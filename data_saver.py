import datetime
import json
import re

from retrying import retry
import requests

from config import API_SERVER, UPLOADER, API_KEY


def check_update_time(conn, link):
    cursor = conn.cursor()
    select_sql = 'SELECT wjw_notice.update_time FROM wjw_notice WHERE wjw_notice.link = "%s" LIMIT 1' % link
    cursor.execute(select_sql)
    exist_item = cursor.fetchall()
    if len(exist_item) == 0:
        return 'insert'
    else:
        publish_time = exist_item[0][0]
        delta = datetime.datetime.now() - publish_time
        if delta <= datetime.timedelta(hours=6):
            return 'pass'
        return 'update'


@retry(stop_max_attempt_number=6, wait_random_min=1, wait_random_max=3)
def update_data(session, province, city, title, date_time:str, content, image, link):
    date_pattern = r'([0-9]{4}-([0-9]{2})-([0-9]{2}))'
    time_pattern = r'([0-1]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    try:
        date = re.findall(date_pattern, date_time)[0][0]
    except:
        date = date_time
    try:
        time = re.findall(time_pattern, date_time)[0][0]
    except:
        time = '00:00:00'

    url = '%s/api/add' % API_SERVER
    data = {
        'province': province,  # str
        'city': city,  # str
        'publish_time': time,  # str
        'publish_date': date,  # str
        'title': title,  # str
        'content': content,  # str
        'link': link,  # str
        'links_to_pic': image,  # str
        'announce_type': 0,  # int
        'uploader': UPLOADER,  # 写自己的ID #str
        'key': API_KEY  # 密钥作为验证权限 #str
    }
    r = session.post(url, data=data)
    if r.status_code != requests.codes.ok:
        print('save error: ', link)
        print(r.status_code)
        print(json.loads(r.text))
    else:
        print(title, 'saved')


