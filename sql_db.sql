create table if not exists mainmenu (
id integer primary key autoincrement,
title text not null,
url text not null,
article_text text not null
);
