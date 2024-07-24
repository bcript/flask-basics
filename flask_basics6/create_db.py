import sqlite3

connection = sqlite3.connect('messages.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS users(message TEXT, author TEXT)"""
cursor.execute(command)