from flask import Flask, render_template, request, redirect, url_for, session, g, jsonify
import sqlite3
import os
from populate_queries import populate_queries
import openpyxl
from openpyxl.utils import get_column_letter
import sqlite3
DATABASE = './data/site.db'


def reload_queries():
    # Drop and recreate queries table
    db=sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS queries')
    cursor.execute('CREATE TABLE queries (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT)')
    with open('data/questions.txt', 'r') as file:
        questions = file.readlines()
        for question in questions:
            cursor.execute('INSERT INTO queries (question) VALUES (?)', [question.strip()])
    db.commit()                

def query_size():
    db=sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM queries')
    myNum=cursor.fetchone()[0]
    myNum=int(myNum)
    return myNum

def query_string():
    Qstring=""
    SignString="?"
    CreateString=""
    myrange=query_size()
    for bobber in range(myrange):
        Qstring+=f", q{bobber+1}"        
        CreateString+=f", q{bobber+1} TEXT NOT NULL"
    if myrange>1:
        for i in range(myrange-1):
            SignString+=f", ?"
    return Qstring, SignString, CreateString

def reload_user_answers(CreateString):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS useranswers')
    cursor.execute(f'CREATE TABLE useranswers (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL{CreateString})')
    db.commit() 

def reload_manager_answers(CreateString):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS manageranswers')
    cursor.execute(f'CREATE TABLE manageranswers (id INTEGER PRIMARY KEY AUTOINCREMENT, managername TEXT NOT NULL, username TEXT NOT NULL{CreateString})')
    db.commit() 