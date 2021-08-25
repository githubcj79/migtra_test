#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
INVOCATION
----------
$ python3 prob_1.py
'''

import json


def walking_json(json_file_name='./data/data1.json'):

	with open(json_file_name) as json_file:
		_list = json.load(json_file)

	for region in _list:
		print(f"{region['name']}")
		for province in region['children']:
			print(f"\t{province['name']}")
			for city in province['children']:
				print(f"\t\t{city['name']}")
				for var, value in city['values'].items():
					print(f"\t\t\t{var} {value}")


	'''
	# Print the type of data variable
	print("Type:", type(data))
	'''


def main():
	walking_json()


if __name__ == '__main__':
	main()