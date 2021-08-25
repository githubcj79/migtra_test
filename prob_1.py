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
	var1_max = 0
	var2_sum = 0

	for region in _list:
		for province in region['children']:
			for city in province['children']:
				for var, value in city['values'].items():
					if var == 'var1':
						var1_sum += int(value)
						var1_show_up += 1
						if region['name'] == 'Region4':
							if int(value) > var1_max:
								var1_max = int(value)
					if province['name'] == 'Provincia2':
						if var == 'var2':
							var2_sum += int(value)

	var1_average = float(var1_sum)/var1_show_up
	return var1_average, var2_sum, var1_max


def main():
	var1_average, var2_sum, var1_max = walking_json()
	print(f"{var1_average}")
	print(f"{var2_sum}")
	print(f"{var1_max}")


if __name__ == '__main__':
	main()