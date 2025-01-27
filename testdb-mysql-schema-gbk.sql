/*创建数据库*/
create database if not exists testdb;

use testdb;

/*用户表*/
create table if not exists user(
    name varchar(20),   /*用户名*/
    userrid int,        /*用户id*/
    primary key(userrid)
);

/*插入初始数据*/
insert into user values('Tom', 1);
insert into user values('Jerry', 2);
/*目录正确下，通过cmd执行mysql -u root -p testdb < testdb-mysql-schema-gbk.sql执行脚本文件*/