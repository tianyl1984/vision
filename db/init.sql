-- 物品
DROP TABLE IF EXISTS item;
CREATE TABLE `item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `code` VARCHAR(10) NULL,
    `name` VARCHAR(100) NULL,
    `type` INTEGER NOT NULL 
);
CREATE UNIQUE INDEX item_code_uindex on item (code);
insert into item(code,name,type) values ('0001','aaa',1);
insert into item(code,name,type) values ('0002','bbb',1);
insert into item(code,name,type) values ('0003','bbb',1);

-- 物品转换关系
DROP TABLE IF EXISTS item_cast;
CREATE TABLE `item_cast` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `from_code` VARCHAR(10) NOT NULL,
    `to_code` VARCHAR(10) NOT NULL,
    `rate` INTEGER NOT NULL 
);
CREATE UNIQUE INDEX item_cast_from_uindex on item_cast (from_code);

insert into item_cast(from_code,to_code,rate) values ('0001','0002',3);
insert into item_cast(from_code,to_code,rate) values ('0002','0003',2);

-- 已有物品数量
DROP TABLE IF EXISTS player_item;
CREATE TABLE `player_item` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `item_code` VARCHAR(10) NOT NULL,
    `quantity` INTEGER NOT NULL,
    `update_time` INTEGER NOT NULL
);
CREATE UNIQUE INDEX player_item_item_code_uindex on player_item (item_code);

insert into player_item(item_code, quantity, update_time) values('0002',3,1);

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
    `item_code` VARCHAR(10) NOT NULL,
    `quantity` INTEGER NOT NULL
);
insert into role_item(role_code,item_code,quantity) values ('C001','0001',1);
insert into role_item(role_code,item_code,quantity) values ('C001','0002',2);
insert into role_item(role_code,item_code,quantity) values ('C001','0003',3);