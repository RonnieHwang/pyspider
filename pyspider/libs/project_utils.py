from datetime import datetime


def get_today_str():
    return datetime.now().strftime('%Y-%m-%d')


def get_today_dt():
    today_str = get_today_str()
    return datetime.strptime(today_str, '%Y-%m-%d')
