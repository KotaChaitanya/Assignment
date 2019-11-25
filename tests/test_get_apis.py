# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:49:39 2019

@author: ck186026
"""

import pytest
import unittest
import requests

class TestCopyTo(unittest.TestCase):
    
    @pytest.mark.positive
    def test_get_locations(self):
        try:
            url = 'http://127.0.0.1:5000/locations'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "[('Perimeter',), ('Center',)]")
    
    @pytest.mark.negative
    def test_get_locations_neg(self):
        try:
            url = 'http://127.0.0.1:5000/location'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.status_code, 404)
        
    @pytest.mark.positive
    def test_get_departments(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "[('Bakery',), ('Deli and Foodservice',), ('Floral',), ('Seafood',)]")
    
    @pytest.mark.negative
    def test_get_ldeparments_neg(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter1/department'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "No Departments exists in the given Location")

    @pytest.mark.positive
    def test_get_categories(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Bakery/category'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "[('Bakery Bread',), ('In Store Bakery',)]")
    
    @pytest.mark.negative
    def test_get_categories_neg(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Bakery1/category'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "No category found in the given Location and Department")

    @pytest.mark.positive
    def test_get_subcategories(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts/subcategory'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "[('Gifts',)]")
    
    @pytest.mark.negative
    def test_get_subcategories_neg(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts1/subcategory'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "No subcategory found in the given Location, Department and Category")

    @pytest.mark.positive
    def test_get_rows(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts/subcategory/Gifts'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "[(22, 'Perimeter', 'Floral', 'Gifts', 'Gifts')]")
    
    @pytest.mark.negative
    def test_get_rows_neg(self):
        try:
            url = 'http://127.0.0.1:5000/locations/Perimeter/department/Floral/category/Gifts1/subcategory/Gifts1'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Exception arised: {}".format(e))
        self.assertEqual(response.text, "No rows found with the given metadata")
