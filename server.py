# -*- coding: utf-8 -*-

from flask import Flask
import sqlite3
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/locations', methods= ['GET', 'POST'])
def get_locations():
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()
        if request.method == 'GET':   
            cur.execute('select distinct(Location) from metadata')
            rows = cur.fetchall()
            if len(rows) == 0:
                rows.append("Metadata doesn't exists")
        elif request.method == 'POST':
          print("Entered into post method")
          mydata=request.get_json(silent=True)
          location = mydata["location"]
          department = mydata["department"]
          category = mydata["category"]
          subcategory = mydata["subcategory"]
          query = "insert into metadata values('{0}', '{1}', '{2}', '{3}')".format(
                  location, department, category, subcategory)        
          cur.execute(query)
          conn.commit()
          rows.append("Added a new metadata to the table")
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    return str(rows)

@app.route('/locations/<location_name>/department')
def get_departments(location_name):
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()  
        query = 'select distinct(department) from metadata where '\
            'Location = "{0}"'.format(location_name)
        print(query)
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) == 0:
            rows.append("No Departments exists in the given Location")
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    return str(rows)

@app.route('/locations/<location_name>/department/'\
           '<department_name>/category', methods= ['GET'])
def get_categories(location_name, department_name):
    
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
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
        print("Connected to database successfully")
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
        print("Connected to database successfully")
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

@app.route('/getskus/locations/<location_name>/department/<department_name>/category'\
           '/<category_name>/subcategory/<subcategory_name>', methods= ['GET'])
def get_skus(location_name, department_name, category_name, subcategory_name):
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        query = 'select * from data where Location '\
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


@app.route('/locations/department', methods= ['PUT'])
def update_department():
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()
        if request.method == 'PUT':
          print("Entered into put method")
          mydata=request.get_json(silent=True)
          location = mydata["location"]
          prev_department = mydata["prev_value_department"]
          update_department = mydata["new_value_for_department"]
          query = "UPDATE metadata SET department = '{0}' WHERE "\
              "location = '{1}' AND department = '{2}';".format(
                      update_department, location, prev_department) 
          print(query)
          cur.execute(query)
          conn.commit()
          rows.append("Updated department with given conditions")
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    return str(rows)

@app.route('/locations/department/category', methods= ['PUT'])
def update_category():
    rows = []
    try:
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()
        if request.method == 'PUT':
          print("Entered into put method")
          mydata=request.get_json(silent=True)
          location = mydata["location"]
          department = mydata["department"]
          prev_category = mydata["prev_category"]
          update_category = mydata["new_value_for_category"]
          query = "UPDATE metadata SET category = '{0}' WHERE "\
              "location = '{1}' AND department = '{2}' and category = '{3}';".format(
                      update_category, location, department, prev_category)
          cur.execute(query)
          conn.commit()
          rows.append("Updated category with given conditions")
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    return str(rows)

@app.route('/locations/department/category/subcategory', methods= ['PUT'])
def update_subcategory():
    try:
        msg = ""
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()
        if request.method == 'PUT':
          print("Entered into put method")
          mydata=request.get_json(silent=True)
          location = mydata["location"]
          department = mydata["department"]
          category = mydata["category"]
          prev_subcategory = mydata["prev_subcategory"]
          update_subcategory = mydata["new_value_for_subcategory"]
          query = "UPDATE metadata SET subcategory = '{0}' WHERE "\
              "location = '{1}' AND department = '{2}' and category = '{3}' and subcategory = '{4}';".format(
                      update_subcategory, location, department, category, prev_subcategory)
          cur.execute(query)
          conn.commit()
          msg = "Updated subcategory with given conditions"
    except Exception as e:
            print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    return msg

@app.route('/deleterows', methods = ["DELETE"])
def delete_rows():
    try:
        msg = ""
        conn = sqlite3.connect('database.db')
        print("Connected to database successfully")
        cur = conn.cursor()
        if request.method == 'DELETE':
            print("Entered into delete method")
            mydata=request.get_json(silent=True)
            location = mydata["location"]
            department = mydata["department"]
            category = mydata["category"]
            subcategory = mydata["subcategory"]
            query = "DELETE FROM metadata WHERE location = '{}' and "\
                    "department = '{}' and category = '{}' and subcategory"\
                    "= '{}';".format(location, department, category, subcategory)
            print(query)
            cur.execute(query)
            conn.commit()
            msg = "Delted matched rows successfully"
    except Exception as e:
        print("Exception : {}".format(e))
    finally:
        if conn:
            conn.close()
    return msg
            
    

if __name__ == '__main__':
        app.run()