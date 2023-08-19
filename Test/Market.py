import numpy as np
import sqlite3
import json
import time


class Market:

    def __init__(self, stocks, bid_step=1, db_name="market"):
        self._bid_step = bid_step  # in percentage
        self._stocks = stocks
        self._db_name = db_name
        self._conn = None  # database connections
        self._cur = None  # database cursor
        self._stock_price = None

        self.init_database()  # initialize the database
        self.load_price()

    def init_database(self):
        self._conn = sqlite3.connect('{}.db'.format(self._db_name))
        self._cur = self._conn.cursor()
        cmd_create_table = ("Create Table active_bids (timetag Integer, virtual_time text, stock_id INTEGER, "
                            "person_id INTEGER, type text check(type IN ('sell','buy')), "
                            "price Numeric, amount INTEGER)")
        try:
            self._cur.execute(cmd_create_table)
        except:
            print("Database already existed")

    def load_price(self):
        self._stock_price = {1: 10, 2: 34, 3: 23}

    def submit_order(self, type, person_id, stock_id, virtual_time, amount):
        # timetag int, virtual_time text, stock_id int, person_id int, type text, price float
        current_time = time.time()
        if type == "buy":
            bid_price = self._stock_price[stock_id] * (1 + self._bid_step / 100)
        else:
            bid_price = self._stock_price[stock_id] * (1 - self._bid_step / 100)
        cmd_insert = "Insert Into active_bids values({},'{}',{},{},'{}',{},{})".format(current_time, "virtual_time",
                                                                                    stock_id, person_id,
                                                                                    type, bid_price, amount)
        print("Order submitted " + cmd_insert)
        self._cur.execute(cmd_insert)
        self._conn.commit()

    def match_order(self):


    # Auxiliary Method
    def close(self):
        self._conn.commit()
        self._conn.close()


if __name__ == "__main__":
    mart = Market(["a", "b", "c"])
    mart.submit_order("buy", 1, 1, "vir", 10)
    mart.submit_order("buy", 1, 2, "vir", 10)
    mart.submit_order("sell", 2, 2, "vir", 10)
    mart.submit_order("sell", 2, 1, "vir", 10)
    mart.close()










