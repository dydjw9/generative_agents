import sqlite3
import json

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def sort():
    myDict = {"ravi": 10, "rajnish": 9, "sanjeev": 15, "yash": 2, "suraj": 32}

    myKeys = list(myDict.keys())
    myKeys.sort()
    sorted_dict = {i: myDict[i] for i in myKeys}
    print(sorted_dict)


def db_operate():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cmd_create_table = "Create Table active_bids (timetag Integer, virtual_time text, stock_id INTEGER, type text check(type IN ('sell','buy')), price float)"
    cur.execute(cmd_create_table)
    cmd_insert = "Insert Into active_bids values({},'{}',{},'{}',{})".format(101, "vir", 1, "buy", 36.87)
    cur.execute(cmd_insert)
    conn.commit()
    conn.close()


def save_json():
    to_save = {1: 10, 2: 34, 3: 23}
    json.dumps(to_save)

def data_parse(inputs):
    for each in inputs:



def db_op2():
    conn = sqlite3.connect('market.db')
    cur = conn.cursor()
    cmd = "select * from active_bids order by price,timetag;"
    cur.execute(cmd)
    results = cur.fetchall()
    print(results)
    conn.commit()
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    db_op2()