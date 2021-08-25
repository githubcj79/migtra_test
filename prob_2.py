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

	A_waiting_seconds = 0
	A_waiting_show_ups = 0
	B_waiting_seconds = 0
	B_waiting_show_ups = 0

	F_show_ups = 0
	F_total_seconds = 0

	# to count the total cycles
	# key <- cycle
	# value <- True if work area is type 2
	cycles = dict()

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

		# El porcentaje de ciclos de faena que incluyeron alguna área de trabajo tipo 2
		if record["cycle"] in cycles:
			cycles[record["cycle"]] = cycles[record["cycle"]] or (record["zone"] in ["AW2", "BW2"])
		else:
			cycles[record["cycle"]] = record["zone"] in ["AW2", "BW2"]

		# El promedio de tiempo en faena F
		if record["zone"] == "F":
			F_show_ups += 1
			F_total_seconds += seconds_elapsed(from_str_to_datetime(record["dt_in"]), 
												from_str_to_datetime(record["dt_out"]))

	A_waiting_average = float(A_waiting_seconds) / A_waiting_show_ups
	B_waiting_average = float(B_waiting_seconds) / B_waiting_show_ups

	cycles_w2 = sum(1 for value in cycles.values() if value)
	cycles_w2_percentage = float(cycles_w2)*100/len(cycles)

	F_average = float(F_total_seconds) / F_show_ups

	return A_waiting_average, B_waiting_average, cycles_w2_percentage, F_average

def main():

	A_waiting_average, B_waiting_average, cycles_w2_percentage, F_average = walking_json()
	print(f"{A_waiting_average} seconds")
	print(f"{B_waiting_average} seconds")
	print(f"{cycles_w2_percentage} %")
	print(f"{F_average/60} minutes")


if __name__ == '__main__':
	main()