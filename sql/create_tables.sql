CREATE TABLE IF NOT EXISTS coindata (
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
    );

CREATE TABLE IF NOT EXISTS coininfo (
    Name VARCHAR(50) PRIMARY KEY REFERENCES coindata (name),
    creator VARCHAR(256),
    creation DATE,
    description VARCHAR(256)
    );
COPY coininfo (Name,creator,creation,description)
FROM '/var/lib/Data/crypto_info.csv'
DELIMITER ','
CSV HEADER;

-- CREATE TABLE IF NOT EXISTS company (
--     uuid VARCHAR(256) PRIMARY KEY,
--     name VARCHAR(256),
--     type VARCHAR(256),
--     primary_role VARCHAR(256),
--     cb_url TEXT,
--     domain VARCHAR(256),
--     homepage_url TEXT,
--     logo_url TEXT,
--     facebook_url TEXT,
--     twitter_url TEXT,
--     linkedin_url TEXT,
--     combined_stock_symbols VARCHAR(256),
--     city VARCHAR(50),
--     region VARCHAR(50),
--     country_code VARCHAR(50),
--     short_description TEXT
--     );
--
