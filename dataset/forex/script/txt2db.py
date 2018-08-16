from datetime import datetime
import os
import sqlite3
import time

DATE_START = '20151230'
DB_NAME = 'xauusd.db'

def parse_time(d, t):
    return time.mktime(datetime.strptime(d + t, "%Y%m%d%H%M%S").timetuple())


def main():
    parent_path = os.path.abspath(os.path.pardir)
    conn = sqlite3.connect(os.path.join(parent_path, 'db', DB_NAME))
    cur = conn.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS History (date INTEGER, coin varchar(20), high FLOAT, low FLOAT, open FLOAT, ' \
          'close FLOAT, volume FLOAT, quoteVolume FLOAT, weightedAverage FLOAT,PRIMARY KEY (date, coin));'
    cur.execute(sql)

    for f_name in os.listdir(os.path.join(parent_path, 'raw_data')):
        if not f_name.endswith('txt'):
            continue

        # coin filter
        if not f_name.startswith('XAU'):
            continue

        f_path = os.path.join(parent_path, 'raw_data', f_name)
        f = open(f_path)
        for line in f.readlines():
            if line.startswith('<'):
                continue

            items = line.split(',')
            coin = items[0]
            d = items[1]

            # date filter: use recent data
            if d < DATE_START:
                continue

            t = items[2]
            open_price = items[3]
            high = items[4]
            low = items[5]
            close = items[6]
            vol = items[7]
            d = parse_time(d, t)

            cur.execute('insert into History values(?,?,?,?,?,?,?,?,?)',
                        (d, coin, high, low, open_price, close, vol, 'NULL', 'NULL'))

    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
