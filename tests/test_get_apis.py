# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:49:39 2019

@author: ck186026
"""

import pytest
import unittest
import requests
import sqlite3
import json
import pandas as pd

class TestCopyTo(unittest.TestCase):
    
#    @pytest.mark.positive
#    def test_get_locations(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "[('Perimeter',), ('Center',)]")
#    
#    @pytest.mark.negative
#    def test_get_locations_neg(self):
#        try:
#            url = 'http://127.0.0.1:5000/location'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.status_code, 404)
#        
#    @pytest.mark.positive
#    def test_get_departments(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "[('Bakery',), ('Deli and Foodservice',), ('Floral',), ('Seafood',)]")
#    
#    @pytest.mark.negative
#    def test_get_deparments_neg(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter1/department'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "['No Departments exists in the given Location']")
#
#    @pytest.mark.positive
#    def test_get_categories(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Bakery/category'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "[('Bakery Bread',), ('In Store Bakery',)]")
#    
#    @pytest.mark.negative
#    def test_get_categories_neg(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Bakery1/category'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "No category found in the given Location and Department")
#
#    @pytest.mark.positive
#    def test_get_subcategories(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts/subcategory'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "[('Gifts',)]")
#    
#    @pytest.mark.negative
#    def test_get_subcategories_neg(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts1/subcategory'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "No subcategory found in the given Location, Department and Category")
#
#    @pytest.mark.positive
#    def test_get_rows(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts/subcategory/Gifts'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "[('Perimeter', 'Floral', 'Gifts', 'Gifts')]")
#    
#    @pytest.mark.negative
#    def test_get_rows_neg(self):
#        try:
#            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts1/subcategory/Gifts1'
#            response = requests.get(url)
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        self.assertEqual(response.text, "No rows found with the given metadata")
#    
#    @pytest.mark.postive
#    def test_post_department(self):
#        try:
#            conn = sqlite3.connect('../database.db')
#            cur = conn.cursor()
#            query = "select count(*) from metadata"
#            cur.execute(query)
#            rows = cur.fetchall()
#            url = 'http://127.0.0.1:5000/locations'
#            data = {
#                	"location":"Hyderabad",
#                	"department":"flowers",
#                	"category":"roses",
#                	"subcategory":"red_roses"
#                    }
#            data = json.dumps(data)
#            requests.post(url, data=data, headers={"Content-Type": "application/json"})
#            #conn.commit()
#            cur.execute(query)
#            expected_rows = cur.fetchall()
#            output = rows[0][0]+1
#            exp = expected_rows[0][0]
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        requests.delete("http://127.0.0.1:5000/deleterows", data=data, headers={"Content-Type": "application/json"})
#        self.assertEqual(output, exp)
#
#    @pytest.mark.positive
#    def test_delete_rows(self):
#        try:
#            conn = sqlite3.connect('../database.db')
#            cur = conn.cursor()
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers",
#            	"category":"roses",
#            	"subcategory":"red_roses"
#            }
#            data = json.dumps(data)
#            requests.post("http://127.0.0.1:5000/locations", data=data, headers={"Content-Type": "application/json"})
#            query = "select count(*) from metadata"
#            cur.execute(query)
#            rows = cur.fetchall()
#            url = 'http://127.0.0.1:5000/deleterows'
#            requests.delete(url, data=data, headers={"Content-Type": "application/json"})
#            conn.commit()
#            cur.execute(query)
#            expected_rows = cur.fetchall()
#            output = rows[0][0]
#            exp = expected_rows[0][0] + 1
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        finally:
#            conn.close()
#        self.assertEqual(output, exp)
#
#    @pytest.mark.positive
#    def test_put_deparment(self):
#        try:
#            conn = sqlite3.connect('../database.db')
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers",
#            	"category":"roses",
#            	"subcategory":"red_roses"
#                }
#            data = json.dumps(data)
#            requests.post("http://127.0.0.1:5000/locations", data=data, headers={"Content-Type": "application/json"})
#            url = 'http://127.0.0.1:5000/locations/department'
#            data = {
#            	"location":"Hyderabad",
#            	"prev_value_department":"flowers",
#            	"new_value_for_department":"flowers and pots",
#                }
#            data = json.dumps(data)
#            requests.put(url, data=data, headers={"Content-Type": "application/json"})
#            res = pd.read_sql_query("select department from metadata where location= 'Hyderabad'", conn)
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers and pots",
#            	"category":"roses",
#            	"subcategory":"red_roses"
#                }
#            data = json.dumps(data)
#            requests.delete("http://127.0.0.1:5000/deleterows", data=data, headers={"Content-Type": "application/json"})
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        finally:
#            conn.close()
#        self.assertEqual(res["Department"][0], "flowers and pots")

#    @pytest.mark.positive
#    def test_put_category(self):
#        try:
#            conn = sqlite3.connect('../database.db')
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers",
#            	"category":"roses",
#            	"subcategory":"blue_marigold"
#                }
#            data = json.dumps(data)
#            requests.post("http://127.0.0.1:5000/locations", data=data, headers={"Content-Type": "application/json"})
#            url = 'http://127.0.0.1:5000/locations/department/category'
#            data = {
#            	"location":"Hyderabad",
#                "department":"flowers",
#            	"prev_category":"roses",
#            	"new_value_for_category":"marigold",
#                }
#            data = json.dumps(data)
#            requests.put(url, data=data, headers={"Content-Type": "application/json"})
#            res = pd.read_sql_query("select category from metadata where location= 'Hyderabad' and department = 'flowers'", conn)
#            print(res)
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers",
#            	"category":"marigold",
#            	"subcategory":"blue_marigold"
#                }
#            data = json.dumps(data)
#            requests.delete("http://127.0.0.1:5000/deleterows", data=data, headers={"Content-Type": "application/json"})
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        finally:
#            conn.close()
#        self.assertEqual(res["Category"][0], "marigold")
#
#    @pytest.mark.positive
#    def test_put_subcategory(self):
#        try:
#            conn = sqlite3.connect('../database.db')
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers",
#            	"category":"marigold",
#            	"subcategory":"red_roses"
#                }
#            data = json.dumps(data)
#            requests.post("http://127.0.0.1:5000/locations", data=data, headers={"Content-Type": "application/json"})
#            url = 'http://127.0.0.1:5000/locations/department/category/subcategory'
#            data = {
#            	"location":"Hyderabad",
#                "department":"flowers",
#            	"category":"marigold",
#                "prev_subcategory":"red_roses",
#                "new_value_for_subcategory":"blue_marigold"
#                }
#            data = json.dumps(data)
#            requests.put(url, data=data, headers={"Content-Type": "application/json"})
#            res = pd.read_sql_query("select subcategory from metadata where location= "\
#                                    "'Hyderabad' and department = 'flowers' and "\
#                                    "category = 'marigold'", conn)
#            data = {
#            	"location":"Hyderabad",
#            	"department":"flowers",
#            	"category":"marigold",
#            	"subcategory":"blue_marigold"
#                }
#            data = json.dumps(data)
#            requests.delete("http://127.0.0.1:5000/deleterows", data=data, headers={"Content-Type": "application/json"})
#        except requests.exceptions.RequestException as e:
#            print("Exception arised: {}".format(e))
#        finally:
#            conn.close()
#        self.assertEqual(res["SubCategory"][0], "blue_marigold")
