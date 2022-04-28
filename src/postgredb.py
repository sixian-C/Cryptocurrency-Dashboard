#!/usr/bin/python
from configparser import ConfigParser
import psycopg2

# this file is used to create and insert data into the Postgre database

def config(filename='config.ini', section='postgresql'):
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



def create_coin_table():
    """ create table in the PostgreSQL database"""
    commands = (
        '''
        CREATE TABLE Cryptocurrency (
            name VARCHAR(80) PRIMARY KEY,
            creator VARCHAR(256), 
            creation_time DATE,
            market_cap BIGINT,
            transaction_volume BIGINT,
            volume_market_cap NUMERIC(9,8),
             description TEXT
             )
        '''
    )
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the database
        cur.close()
        print('Cryptocurrency Data table created')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def copy_coindata(data):
    """ insert multiple department into the departments table  """
    f = open(r'cryptocurrency(1).csv', 'r')

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.copy_from(f, 'Cryptocurrency', sep=',')
        f.close()
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

def insert_coindata(data):
    """ insert multiple department into the departments table  """
    sql = """ INSERT INTO Cryptocurrency (name, creator, creation_time, market_cap, transaction_volume, volume_market_cap, description) 
                           VALUES (%s,%s,%s,%s,%s,%s,%s) """
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

# Function to update single variable (transaction_volume)
def updateTrans(data):
    sql =  """Update Cryptocurrency set transaction_volume = %s where name = %s"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, data)
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

# Function to update single variable (volume_market_cap)
def updateVolume(data):
    sql = """Update Cryptocurrency set volume_market_cap = %s where name = %s"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, data)
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


def insert_data():
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(
            "INSERT into Cryptocurrency VALUES('Bitcoin', 'Satoshi Nakamoto', '1/9/2009', '790833172478','31122451921', '0.03935400', 'Bitcoin  is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries. Transactions are verified by network nodes through cryptography and recorded in a public distributed ledger called a blockchain.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Ethereum', 'Vitalik Buterin & Gavin Wood', '7/30/2015', '369528463294', '18233276543', '0.04934201','Ethereum is a decentralized, open-source blockchain with smart contract functionality. Unlike Bitcoin, it wasn’t created to be digital money. Instead, Ethereum’s founders set out to build a new kind of global, decentralized computing platform that takes the security and openness of blockchains and extends those attributes to a vast range of applications.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Tether', 'Brock Pierce & Craig Sellars', '10/6/2014', '83016904420','69234155152', '0.83397659', 'Tether (often called by its symbol USDT) is a cryptocurrency that is hosted on the Ethereum and Bitcoin blockchains, among others. Tether is called a stablecoin because it was originally designed to always be worth US$1.00, maintaining $1.00 in reserves for each tether issued.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('USD Coin', 'Circle Company', '5/15/2018', '49892096860', '4161086121', '0.08340171','Ethereum is a decentralized, open-source blockchain with smart contract functionality. Unlike Bitcoin, it wasn’t created to be digital money. Instead, Ethereum’s founders set out to build a new kind of global, decentralized computing platform that takes the security and openness of blockchains and extends those attributes to a vast range of applications.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('XRP', 'Ripple Company', '5/15/2018', '36221302539','1792254133', '0.04948066', 'XRP is known as the native cryptocurrency employed by ripples, a US-based technology company and a real-time gross settlement system, currency exchange and remittance network created by Ripple Labs Inc.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('SOL', 'Anatoly Yakovenko, Greg Fitzgerald, Stephen Akridge, Raj Gokal', '4/1/2019', '35498719727', '1657494115', '0.04669166','SOL is the native cryptocurrency of Solana, a public blockchain platform with smart contract functionality.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('ADA', 'Charles Hoskinson', '9/27/2017', '790833172478','31122451921', '0.03935400', 'ADA is the internal cryptocurrency of Cardano, a public blockchain platform which is  open-source and decentralized, with consensus achieved using proof of stake.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Terra', 'Daniel Shin & Do Kwon', '1/1/2018', '34422519580', '2144157919', '0.06228939','Terra is a price-stable cryptocurrency that aims to power the next-generation payment network and grow the real GDP of the blockchain economy.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('AVAX', 'Emin Gün Sirer, Kevin Sekniqi, Maofan “Ted” Yin', '9/1/2020', '20905919675','482111672', '0.02306101', 'Avalanche is a decentralized, open-source proof of stake blockchain with smart contract functionality. AVAX is the native cryptocurrency of the platform.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Dogecoin', 'Billy Markus, Jackson Palmer', '12/6/2013', '18720995678', '731297348', '0.03958512','Dogecoin.com promotes the currency as the fun and friendly Internet currency, referencing its origins as a joke. Software engineers Billy Markus and Jackson Palmer launched the satirical cryptocurrency as a way to make fun of Bitcoin and the many other cryptocurrencies boasting grand plans to take over the world.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Polkadot', 'Gavin Wood', '5/26/2020', '18720995678', '725134006', '0.03873373','Polkadot is an open source, blockchain platform and cryptocurrency.It provides interconnectivity and interoperability between blockchains, by enabling independent chains to securely exchange messages and perform transactions with each other without trusted third-party.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Dai', 'Rune Christensen', '12/18/2017', '9080837900','387674744', '0.04269152', 'Dai is a stablecoin cryptocurrency which aims to keep its value as close to one United States dollar (USD) as possible through an automated system of smart contracts on the Ethereum blockchain.Dai is maintained and regulated by MakerDAO, a decentralized autonomous organization (DAO) composed of the owners of its governance token, MKR, who may vote on changes to certain parameters in its smart contracts in order to ensure the stability of Dai.')")

        cur.execute(
            "INSERT into Cryptocurrency VALUES('Litecoin', 'Charlie Lee', '10/7/2011', '7811975828', '671569694', '0.08596669','Litecoin is a peer-to-peer cryptocurrency and open-source software project released under the MIT/X11 license. Litecoin was an early bitcoin spinoff or altcoin, starting in October 2011. In technical details, Litecoin is nearly identical to Bitcoin.')")

        conn.commit()
        # close communication with the database
        cur.close()
        print("Company Data successfully inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
