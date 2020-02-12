import re
import time

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from newspaper import Article
from retrying import retry

from config import url_list
from data_saver import update_data


session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
}


class Page404Error(FileExistsError):
    pass


@retry(stop_max_attempt_number=6, wait_random_min=10, wait_random_max=30)
def parse_notice_list(url):
    """
    解析新闻列表
    :param url: 列表页的url
    :return: [dict：title，create_time, url]
    """

    def parse_list(wide_list):
        """根据是否包含时间筛选"""
        filter_list = []
        for i in wide_list:
            # 过滤掉不包含时间的
            date_pattern = r'((\d{4}(-|年|\.|/))?\d{1,2}(-|月|\.|/)\d{1,2}日?)'
            dates = re.findall(date_pattern, i.text)
            if len(dates) >= 1:
                create_time = dates[0][0]
                titles = i.find_all('a')
                for j in titles:
                    title = j.text
                    if len(title) != 0:
                        break
                if len(title) == 0:
                    continue
                try:
                    detail_url = i.find('a').get('href')
                except:
                    continue
                detail_url = urljoin(url, detail_url)
                create_time = create_time.replace('.', '-')
                create_time = create_time.replace('/', '-')
                create_time = create_time.replace('年', '-')
                create_time = create_time.replace('月', '-')
                create_time = create_time.replace('日', '')
                if len(create_time) == 5:
                    # need to add year
                    if create_time[0:3] in ('01-', '02-'):
                        create_time = '2020-' + create_time
                    else:
                        create_time = '2019-' + create_time

                filter_list.append({
                    'title': title,
                    'create_time': create_time,
                    'url': detail_url
                })
        if len(filter_list) <= 6:
            filter_list = []
        return filter_list

    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, features="lxml")
    if 'Produced By 大汉网络 大汉版通发布系统' in soup.text:
        api_url_pattern = r'<nextgroup><!\[CDATA\[<a href="([^"]+)"></a>]]></nextgroup>'
        api_url = re.findall(api_url_pattern, soup.text)[0]
        api_url = urljoin(url, api_url)
        xml_content = requests.get(api_url, headers=headers).content
        xml_soup = BeautifulSoup(xml_content, 'xml')
        records = xml_soup.find_all('record')
        wide_list = [BeautifulSoup(i.text, 'lxml') for i in records]
        filter_list = parse_list(wide_list)
        # 某些栏目可能通知较多，比如盘锦市有301条
        if len(filter_list) > 20:
            filter_list = filter_list[0:20]

    else:
        # normal html
        # TODO: 先找ul，选择下面含li最多的ul
        avaliable_tag = ('li', 'tr')
        filter_list = []
        for tag in avaliable_tag:
            wide_list = soup.find_all(tag)
            if len(wide_list) <= 10:
                continue
            filter_list = parse_list(wide_list)
            # ignore notice list if num is less than 5
            if len(filter_list) >= 6:
                break

    print(province, city, 'get %s news' % len(filter_list))
    return filter_list


def compare_strs(str1, str2):
    if str1 != str2:
        print('old:new', str1, str2)


@retry(stop_max_attempt_number=9, wait_random_min=10, wait_random_max=20)
def parse_notice_detail(url, title='', create_time=''):
    """
    解析新闻正文
    :param url: 完整的详情页url
    :param create_time: 列表页解析到的日期
    :param title: 列表页解析到的标题
    :return: tuple: title, create_time, content, pic_link
    """
    article = Article(url, language='zh')
    try:
        article.download()
        article.parse()
    except Exception as e:
        if 'failed with 404' in str(e):
            raise Page404Error
    parse_time = article.meta_data.get('published', '')
    if len(parse_time) > len(create_time):
        create_time = parse_time
    return title.strip(), create_time, article.text, article.top_image


def clean_top_image():
    """
    根据同一网站下top image重复的次数来判断，当一张图片重复3次及以上时，认为其是背景图片，予以删除
    :return:
    """
    pass


if __name__ == '__main__':
    for province, province_data in url_list.items():
        # if province == '吉林省':
        #     continue
        for city, city_urls in province_data.items():
            # if city != '白山市':
            #     continue
            for list_url in city_urls:
                urls = parse_notice_list(list_url)
                for i in urls:
                    try:
                        title, create_time, content, image = parse_notice_detail(i['url'], i['title'], i['create_time'])
                    except Page404Error:
                        print(i['url'], '404')
                        continue
                    else:
                        update_data(session, province, city, title, create_time, content, image, i['url'])
                        time.sleep(5)
