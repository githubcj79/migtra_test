#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
INVOCATION
----------
$ python3 prob_2.py
'''

from datetime import datetime

import json

def from_str_to_datetime():
	# str_in = "2019-01-01T00:08:55"
	str_in = "2019-01-01T02:08:55"
	date_ = datetime.strptime(str_in, '%Y-%m-%dT%H:%M:%S')
	str_out = date_.strftime("'%b %d %Y %I:%M%p'")

	print(f"{str_in}")
	print(f"{str_out}")


def walking_json(json_file_name='./data/data2.json'):

	with open(json_file_name) as json_file:
		_list = json.load(json_file)

	print(f"{type(_list)}")

	for record in _list:
		pass

def main():
	# walking_json()
	from_str_to_datetime()


if __name__ == '__main__':
	main()