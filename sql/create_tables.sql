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