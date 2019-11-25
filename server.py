# -*- coding: utf-8 -*-

from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/locations')
def get_locations():
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()
        cur.execute('select distinct(Location) from metadata')
        rows = cur.fetchall()
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    if len(rows) == 0:
        return "Metadata doesn't exist"
    else:
        return str(rows)


@app.route('/locations/<location_name>/department', methods= ['GET'])
def get_departments(location_name):
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        query = 'select distinct(department) from metadata where '\
                'Location = "{0}"'.format(location_name)
        print(query)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    if len(rows) == 0:
        return "No Departments exists in the given Location"
    else:
        return str(rows)


@app.route('/locations/<location_name>/department/'\
           '<department_name>/category', methods= ['GET'])
def get_categories(location_name, department_name):
    
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Opened database successfully")
        query = 'select distinct(category) from metadata where Location '\
        '= "{0}" AND department= "{1}"'.format(location_name, department_name)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    if len(rows) == 0:
        return "No category found in the given Location and Department"
    else:
        return str(rows)

@app.route('/locations/<location_name>/department/<department_name>'\
           '/category/<category_name>/subcategory', methods= ['GET'])
def get_subcategories(location_name, department_name, category_name):
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Opened database successfully")
        query = 'select distinct(subcategory) from metadata where Location '\
        '= "{0}" AND department= "{1}" AND category = "{2}"'.format(location_name, department_name, category_name)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    if len(rows) == 0:
        return "No subcategory found in the given Location, Department and Category"
    else:
        return str(rows)

@app.route('/locations/<location_name>/department/<department_name>/category'\
           '/<category_name>/subcategory/<subcategory_name>', methods= ['GET'])
def get_metadata_rows(location_name, department_name, category_name, subcategory_name):
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Opened database successfully")
        query = 'select * from metadata where Location '\
                '= "{0}" AND department= "{1}" AND category = "{2}" AND subcategory = '\
                '"{3}"'.format(location_name, department_name, category_name, subcategory_name)
        print(query)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    if len(rows) == 0:
        return "No rows found with the given metadata"
    else:
        return str(rows)

if __name__ == '__main__':
        app.run()