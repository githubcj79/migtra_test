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

	# print(f"{type(_list)}")

	A_waiting_seconds = 0
	A_waiting_show_ups = 0

	B_waiting_seconds = 0
	B_waiting_show_ups = 0

	for record in _list:
		# El promedio de tiempo de espera en zonas A
		if record["zone"] in ["AE1", "AE2"]:
			A_waiting_show_ups += 1
			A_waiting_seconds += seconds_elapsed(from_str_to_datetime(record["dt_in"]), 
												from_str_to_datetime(record["dt_out"]))

		# El promedio de tiempo de espera en zonas B
		if record["zone"] in ["BE1", "BE2"]:
			B_waiting_show_ups += 1
			B_waiting_seconds += seconds_elapsed(from_str_to_datetime(record["dt_in"]), 
												from_str_to_datetime(record["dt_out"]))

	# print(f"{A_waiting_show_ups} {A_waiting_seconds}")
	A_waiting_average = float(A_waiting_seconds) / A_waiting_show_ups
	# print(f"{A_waiting_average} seconds")

	# print(f"{B_waiting_show_ups} {B_waiting_seconds}")
	B_waiting_average = float(B_waiting_seconds) / B_waiting_show_ups
	# print(f"{B_waiting_average} seconds")

	return A_waiting_average, B_waiting_average

def main():

	# date_1 = from_str_to_datetime("2019-01-01T00:05:59")
	# date_2 = from_str_to_datetime("2019-01-01T00:08:55")
	# print(f"seconds elapsed: {seconds_elapsed(date_1, date_2)}")

	A_waiting_average, B_waiting_average = walking_json()
	print(f"{A_waiting_average} seconds")
	print(f"{B_waiting_average} seconds")


if __name__ == '__main__':
	main()