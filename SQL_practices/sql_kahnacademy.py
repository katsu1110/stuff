# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:43:28 2018

contents summary from Kahn academy's SQL course

@author: katsuhisa
"""

#%%
# SQL 1 hour course from Kahn academy
'''Grocery list:
    Bananas (4)
    Peanut Butter (1)
    Dark Chocolate Bars (2)
    ...
    '''
    
Query = '''
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER);

INSERT INTO groceries VALUES (1, "Bananas", 4, 7);
INSERT INTO groceries VALUES (2, "Peanut Butter", 1, 2);
INSERT INTO groceries VALUES (2, "Dark chocolate bars", 2, 2);
INSERT INTO groceries VALUES (2, "Ice cream", 1, 12);
INSERT INTO groceries VALUES (2, "Cherries", 6, 2);
INSERT INTO groceries VALUES (2, "Chocolate syrup", 1, 4);

SELECT * FROM groceries;
SELECT * FROM groceries ORDER BY aisle;
SELECT * FROM groceries WHERE aisle > 5 ORDER BY aisle;

SELECT SUM(quantity) FROM groceries;
SELECT MAX(quantity) FROM groceries;

SELECT aisle, SUM(quantity) FROM groceries GROUP BY aisle;

'''

Query = '''
CREATE TABLE exercise_logs 
    (id INTEGER PRIMARY KEY, AUTOINCREMENT, 
    
    type TEXT, 
    minutes INTEGER, 
    calories INTEGER,
    heart_rate INTEGER);

INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 30, 100, 105);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("biking", 10, 30, 105);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("dancing", 15, 200, 120);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("tree climbing", 30, 70, 90);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("tree climbing", 25, 72, 80);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("rowing", 30, 70, 90);
INSERT INTO exercise_logs(type, minutes, calories, heart_rate) VALUES ("hiking", 60, 80, 85);

SELECT * FROM exercise_logs;
SELECT * FROM exercise_logs WHERE calories > 50 ORDER BY calories;
SELECT * FROM exercise_logs WHERE calories > 50 AND minutes < 30;
SELECT * FROM exercise_logs WHERE calories > 50 OR heart_rate > 100;
SELECT * FROM exercise_logs WHERE type = "biking" OR type = "hiking";
SELECT * FROM exercise_logs WHERE type IN ("biking", "hiking", "tree climbing", "rowing");
SELECT * FROM exercise_logs WHERE type NOT IN ("biking", "hiking", "tree climbing", "rowing");

'''