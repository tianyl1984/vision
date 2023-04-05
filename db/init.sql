-- 物品
DROP TABLE IF EXISTS item;
CREATE TABLE `item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `code` VARCHAR(10) NULL,
    `name` VARCHAR(100) NULL,
    `type` INTEGER NOT NULL 
);
CREATE UNIQUE INDEX item_code_uindex on item (code);

-- 物品转换关系
DROP TABLE IF EXISTS item_cast;
CREATE TABLE `item_cast` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `from` INTEGER NOT NULL,
    `to` INTEGER NOT NULL,
    `rate` INTEGER NOT NULL 
);

-- 已有物品数量
DROP TABLE IF EXISTS player_item;
CREATE TABLE `player_item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `item_id` INTEGER NOT NULL,
    `quantity` INTEGER NOT NULL,
    `update_time` INTEGER NOT NULL
);
CREATE UNIQUE INDEX player_item_item_id_uindex on player_item (item_id);

-- 角色
DROP TABLE IF EXISTS player_role;
CREATE TABLE `player_role` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `code` VARCHAR(10) NOT NULL,
    `name` VARCHAR(50) NOT NULL
);
CREATE UNIQUE INDEX player_role_code_uindex on player_role (code);

insert into player_role(code,name) values ('C001','纳西妲');

-- 角色升级需要的物品
DROP TABLE IF EXISTS role_item;
CREATE TABLE `role_item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `role_code` VARCHAR(10) NOT NULL,
    `item_id` INTEGER NOT NULL,
    `quantity` INTEGER NOT NULL
);
