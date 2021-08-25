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

	var1_sum = 0
	var1_show_up = 0

	var2_sum = 0

	for region in _list:
		print(f"{region['name']}")
		for province in region['children']:
			print(f"\t[{province['name']}]")
			for city in province['children']:
				print(f"\t\t{city['name']}")
				for var, value in city['values'].items():
					print(f"\t\t\t{var} {value}")
					if var == 'var1':
						# print(f"\t\t\t{var} {value}")
						var1_sum += int(value)
						var1_show_up += 1
					if province['name'] == 'Provincia2':
						if var == 'var2':
							var2_sum += int(value)
							# print(f"\t\t\t{var2_sum}")

	var1_average = float(var1_sum)/var1_show_up
	# print(f"{var1_sum} {var1_show_up} {var1_average}")

	print(f"{var2_sum}")

	'''
	# Print the type of data variable
	print("Type:", type(data))
	'''


def main():
	walking_json()


if __name__ == '__main__':
	main()