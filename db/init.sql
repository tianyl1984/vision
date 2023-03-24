DROP TABLE IF EXISTS item;
CREATE TABLE `item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `code` VARCHAR(10) NULL,
    `name` VARCHAR(100) NULL,
    `type` INTEGER NOT NULL 
);
CREATE UNIQUE INDEX item_code_uindex on item (code);

INSERT INTO item (code, name, type) VALUES ('00001', '中文test', 1);
INSERT INTO item (code, name, type) VALUES ('00002', 'abc', 1);

DROP TABLE IF EXISTS item_cast;
CREATE TABLE `item_cast` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `from` INTEGER NOT NULL,
    `to` INTEGER NOT NULL,
    `rate` INTEGER NOT NULL 
);

DROP TABLE IF EXISTS player_item;
CREATE TABLE `player_item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `item_id` INTEGER NOT NULL,
    `quantity` INTEGER NOT NULL,
    `update_time` INTEGER NOT NULL
);
CREATE UNIQUE INDEX player_item_item_id_uindex on player_item (item_id);

INSERT INTO player_item (id, item_id, quantity, update_time) VALUES (1, 1, 20, 1679451810);

DROP TABLE IF EXISTS player_role;
CREATE TABLE `player_item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `item_id` INTEGER NOT NULL,
    `quantity` INTEGER NOT NULL,
    `update_time` INTEGER NOT NULL
);