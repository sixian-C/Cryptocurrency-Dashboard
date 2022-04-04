#!/usr/bin/python
from configparser import ConfigParser
import psycopg2
def config(filename='src/config.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
import csv

def connect():
    """ Connect to the PostgreSQL database server """
    global conn
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

#!/usr/bin/python
'''
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE coindata (
                coin_idx SERIAL PRIMARY KEY,
                id VARCHAR(50) NOT NULL ,
                rank INT NOT NULL,
                symbol VARCHAR(50) NOT NULL,
                name VARCHAR(50) NOT NULL,
                supply NUMERIC,
                maxSupply NUMERIC,
                marketCapUsd NUMERIC,
                volumeUsd24Hr NUMERIC,
                priceUsd NUMERIC,
                changePercent24Hr NUMERIC,
                vwap24Hr NUMERIC,
                explorer text,
                timestamp timestamp with time zone
                )
        """
    )
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Execution completed, Table created")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
'''
def insert_coindata(data):
    """ insert multiple department into the departments table  """
    sql = '''INSERT INTO coindata (id,rank,symbol,name,supply,maxSupply,marketCapUsd,volumeUsd24Hr,priceUsd,changePercent24Hr,vwap24Hr,explorer,timestamp) 
    VALUES (%(id)s,%(rank)s,%(symbol)s,%(name)s,%(supply)s,
            %(maxSupply)s,
            %(marketCapUsd)s,
            %(volumeUsd24Hr)s,
            %(priceUsd)s,
            %(changePercent24Hr)s,
            %(vwap24Hr)s,
            %(explorer)s,
            now()
        );'''
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,data)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        print("Cryptocurrency Data successfully inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def insert_company_data(data):
    """ insert multiple department into the departments table  """
    sql = '''INSERT INTO company (uuid,name,type,primary_role,cb_url,domain,homepage_url,logo_url,facebook_url,twitter_url,linkedin_url,combined_stock_symbols,city,region,country_code,short_description)
    VALUES (%(uuid)s,%(name)s,%(type)s,%(primary_role)s,%(cb_url)s,
            %(domain)s,
            %(homepage_url)s,
            %(logo_url)s,
            %(facebook_url)s,
            %(twitter_url)s,
            %(linkedin_url)s,
            %(combined_stock_symbols)s,
            %(city)s,
            %(region)s,
            %(country_code)s,
            %(short_description)s
        );'''
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,data)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        print("Company Data successfully inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
