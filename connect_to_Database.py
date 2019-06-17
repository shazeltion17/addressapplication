import numpy as np
import pandas as pd
import psycopg2

def get_data(data):
    cur, con = build_connection()
    run_sql(cur, con, data)
    return data

def build_connection():
    conn = psycopg2.connect(host="tableaudatainstance.cotqt9fi7tuv.us-west-2.rds.amazonaws.com", dbname="postgres", user="Samuel", password="thecatranfast")
    cur = conn.cursor()
    # print cur
    return cur, conn


def run_sql(cur, conn, data):
    sql = 'INSERT INTO "Address_Application"."Address" (full_street, state, zip_code, street_name, street_number) VALUES'
    data = [tuple(x) for x in data.values]
    print(data)
    args_str = b",".join(cur.mogrify('(%s, %s, %s, %s, %s)', x) for x in data).decode('utf-8')
    #args_str = ','.join(cur.mogrify("(%s,%s,%s,%s,%s)", x) for x in data)
    sql = (sql + args_str)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return