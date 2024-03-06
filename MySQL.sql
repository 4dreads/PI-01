CREATE DATABASE steam_games;

USE steam_games;

CREATE TABLE steam_games (
    id INT PRIMARY KEY,
    publisher VARCHAR(255),
    genres VARCHAR(255),
    app_name VARCHAR(255),
    title VARCHAR(255),
    url VARCHAR(255),
    release_date DATE,
    tags VARCHAR(255),
    discount_price DECIMAL(10,2),
    reviews_url VARCHAR(255),
    specs VARCHAR(255),
    price DECIMAL(10,2),
    early_access BOOLEAN,
    developer VARCHAR(255),
    metascore INT
);

CREATE TABLE user_items (
    user_id VARCHAR(255),
    user_url VARCHAR(255),
    item_id VARCHAR(255),
    item_name VARCHAR(255),
    playtime_forever INT,
    playtime_2weeks INT,
    PRIMARY KEY (user_id, item_id)
);

CREATE TABLE user_reviews (
    user_id VARCHAR(255),
    user_url VARCHAR(255),
    reviews JSON,
    FOREIGN KEY (user_id) REFERENCES user_items(user_id)
);
INSERT INTO steam_games (
    id, publisher, genres, app_name, title, url, release_date, tags, discount_price, reviews_url, specs, price, early_access, developer, metascore
) VALUES (
    761140, '["Kotoshiro"]', '["Action", "Adventure"]', 'The Dream Machine: Chapter 4', 'The Dream Machine: Chapter 4', 'http://store.steampowered.com/app/761140/Lost_Summoner_Kitty/', '2018-01-04', '["Simulation", "Indie", "Action", "Adventure", "Funny", "Open World", "First-Person", "Sandbox", "Free to Play"]', 22.66, 'http://steamcommunity.com/app/761140/reviews/?browsefilter=mostrecent&p=1', '["Multi-player", "Co-op", "Cross-Platform Multiplayer", "Downloadable Content"]', 4.99, false, '["Degica"]', 80
);

INSERT INTO steam_games (
    id, publisher, genres, app_name, title, url, release_date, tags, discount_price, reviews_url, specs, price, early_access, developer, metascore
) VALUES (
    643980, '["Secret Level SRL"]', '["Action", "Adventure", "RPG"]', 'Fate/EXTELLA - The Umbral Star', 'Fate/EXTELLA - The Umbral Star', 'http://store.steampowered.com/app/643980/FATE_EXTELLA_The_Umbral_Star/', '2017-01-19', '["Action", "Anime", "Hack and Slash", "Sexual Content", "Violent"]', 0.49, 'http://steamcommunity.com/app/643980/reviews/?browsefilter=mostrecent&p=1', '["Single-player", "Steam Achievements", "Steam Cloud", "Steam Trading Cards"]', 9.99, false, '["Marvelous Inc."]', 74
);

INSERT INTO steam_games (
    id, publisher, genres, app_name, title, url, release_date, tags, discount_price, reviews_url, specs, price, early_access, developer, metascore
) VALUES (
    670290, '["Poolians.com"]', '["Strategy"]', 'Fate/EXTELLA - Link', 'Fate/EXTELLA - Link', 'http://store.steampowered.com/app/670290/FateEXTELLA_Link/', '2017-08-25', '["Action", "Anime", "Free to Play"]', 0.69, 'http://steamcommunity.com/app/670290/reviews/?browsefilter=mostrecent&p=1', '["Single-player", "Steam Achievements", "Steam Cloud", "Steam Trading Cards"]', 0, false, '["Marvelous Inc."]', 77
);

SELECT * FROM steam_games
ORDER BY metascore DESC
LIMIT 1;
