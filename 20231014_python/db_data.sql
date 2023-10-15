create database `sales`;

use `sales`;
create table `sales`(
	`id` int not null auto_increment,
	`goods` varchar(45) default null,
	`price` int default null,
	`buy_date` date default null,
    primary key (`id`)
);

insert into sales (goods, price, buy_date) values ('りんご', '100', '2023-10-01');
insert into sales (goods, price, buy_date) values ('ばなな', '120', '2023-10-01');
insert into sales (goods, price, buy_date) values ('りんご', '100', '2023-10-02');
insert into sales (goods, price, buy_date) values ('りんご', '100', '2023-10-02');
insert into sales (goods, price, buy_date) values ('りんご', '100', '2023-10-02');
insert into sales (goods, price, buy_date) values ('ばなな', '120', '2023-10-02');
insert into sales (goods, price, buy_date) values ('ばなな', '120', '2023-10-02');