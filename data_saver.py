import datetime


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


def update_data(conn, province, city, title, time, content, image, link, operate):
    cursor = conn.cursor()
    try:
        if operate == 'insert':
            insert_sql = '''INSERT INTO `wjw_notice` (`province`, `city`, `publish_time`, `title`, `content`, `link`, `links_to_pic`, `update_time`, `owner`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')''' % (province, city, time, title, content, link, image, datetime.datetime.now(), '小爪')
            # print(insert_sql)
            cursor.execute(insert_sql)
            conn.commit()
            print(title, 'inserted')
        elif operate == 'update':
            update_sql = '''UPDATE `wjw_notice` SET `title`='%s', `content`='%s', `links_to_pic`='%s', `publish_time`='%s', `update_time`='%s' WHERE (`link`='%s')
            ''' % (title, content, image, time, datetime.datetime.now(), link)
            cursor.execute(update_sql)
            conn.commit()
            print(title, 'updated')
    except Exception as e:
        if 'Incorrect datetime value' in str(e):
            return
        else:
            print(e)


