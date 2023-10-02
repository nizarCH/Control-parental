import time
from datetime import datetime
from app_blocker import *
from site_Blocker import *
from time import sleep
import mysql.connector as con


db = con.connect(host="localhost", user="root", password="", db="pfl")
cursor = db.cursor()


def gTime(con=None):
    dns_change()
    while True:
        t= dt.now().strftime('%Y-%m-%d %H:%M:%S')
        print("time == ",t)
        # id, s, e = (select id, s, e where s <= dt.now and dt.now() < e)
        try:
            cursor.execute(f"select idK,timeDebut,timeFin from times where timeDebut <= '{t}'  and '{t}'  < timeFin")
            id , s, e = cursor.fetchone()
        except:
            sleep(3)
            continue

        print("*******************************************************")
        print(id,ascii(s),ascii(e))

        print(type(e),type(s))
        s = datetime.strptime(s.strip(), '%Y-%m-%d %H:%M:%S')
        e = datetime.strptime(e, '%Y-%m-%d %H:%M:%S')

        print("nizar")

        cursor.execute(f"select nomSite from blocksiteweb where idK={id}")
        sites = cursor.fetchall()
        print(sites)

        cursor.execute(f"select nomApp from blockapp where idK={id}")
        apps = cursor.fetchall()
        print(apps)
        sites = [site[0] for site in sites]
        apps = [app[0] for app in apps]
        if s and e:
            for i in apps:
                if i:
                    iThread = threading.Thread(target=kill_app, args=(i, s, e))
                    iThread.start()

        # block_site(sites, s, e)
        iThread = threading.Thread(target=block_websites, args=(sites,s, e))
        # iThread.daemon = True
        iThread.start()

        while s <= dt.now() and dt.now() <= e:
            print(f'Still blocking for id = {id}')
            sleep(3)

        # break