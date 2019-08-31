import datetime
from sqlalchemy import create_engine


db_connect = create_engine('sqlite:///ewxDB.db')


def create_url(url, shortcode):
    now = datetime.datetime.now().isoformat()
    conn = db_connect.connect()
    conn.execute("INSERT INTO Url_Shorten (Url, ShortCode, CreatedAt, LastRedirect, RedirectCount) "
                 "VALUES ('{}', '{}', '{}', '{}', '{}');".format(url, shortcode, now, now, 1))


def get_shortcode(shortcode):
    conn = db_connect.connect()
    query = conn.execute("SELECT * FROM Url_Shorten where ShortCode='{}'".format(shortcode))
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return result


def update_shortcode(shortcode):
    now = datetime.datetime.now().isoformat()
    conn = db_connect.connect()
    redirect_count = get_shortcode(shortcode)['data'][0]['RedirectCount']
    redirect_count += 1
    conn.execute("UPDATE Url_Shorten SET RedirectCount= '{}', LastRedirect = '{}'  WHERE ShortCode = '{}'"
                 .format(redirect_count, now, shortcode))


def delete_shortcode_for_test(shortcode):
    conn = db_connect.connect()
    conn.execute("DELETE FROM Url_Shorten WHERE ShortCode = '{}';"
                 .format(shortcode))