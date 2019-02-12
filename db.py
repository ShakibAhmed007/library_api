from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


"""
CREATE TABLE library(
 id serial PRIMARY KEY,
 name VARCHAR (50) NOT NULL,
 location VARCHAR (50) NOT NULL,
 email VARCHAR (50) UNIQUE NOT NULL,
 owner_name VARCHAR(50) NOT NULL,
 owner_email VARCHAR(100) Not Null,
 rating INTEGER
);
"""