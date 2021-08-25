#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
INVOCATION
----------
$ python3 prob_2.py
'''

from datetime import datetime

import json

def from_str_to_datetime(str_in):
	return datetime.strptime(str_in, '%Y-%m-%dT%H:%M:%S')

def seconds_elapsed(datetime_1, datetime_2):
	'''
	It is taken datetime_2 > datetime_1.
	'''
	return (datetime_2 - datetime_1).total_seconds()


def walking_json(json_file_name='./data/data2.json'):

	with open(json_file_name) as json_file:
		_list = json.load(json_file)

	print(f"{type(_list)}")

	for record in _list:
		pass

def main():
	# walking_json()
	# from_str_to_datetime()
	date_1 = from_str_to_datetime("2019-01-01T00:05:59")
	date_2 = from_str_to_datetime("2019-01-01T00:08:55")
	print(f"seconds elapsed: {seconds_elapsed(date_1, date_2)}")


if __name__ == '__main__':
	main()