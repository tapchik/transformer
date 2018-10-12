#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Эта программа переводит (трансформирует) число из одной системы счисления в другую

variables = {"number": "0", "base_0": 0, "base_1": 0}
alphabet = {}
	
def init_varibles():
	
	to_return = {}
	
	user_input = input("Введите число, которое хотите перевести: ")
	to_return["number"] = user_input
	
	user_input = input("Его нынишнее основание: ")
	to_return["base_0"] = int(user_input)
	
	user_input = input("Желаемое основание: ")
	to_return["base_1"] = int(user_input)
	
	return to_return #returns new set of variables

def generate_alphabet (base_0, base_1):
	
	if base_0 > base_1: 
		base = base_0
	elif base_0 <= base_1:
		base = base_1
	
	if base <= 10:
		return {}
	
	to_return = {}
	
	for i in range(10, base):
		to_return[i] = chr(55+i)
		
	return to_return

def power(x, y): #возводит x в степень y
	return int(x)**int(y)

def num_to_list (num):
	digits = [x for x in num]
	for i in range(len(digits)): 
		if ord(digits[i]) >= 65 and ord(digits[i]) <= 90:
			digits[i] = ord(digits[i])-55
		else: digits[i] = int(digits[i])
	return digits

def list_to_num (seq):
	seq.reverse()
	for i in range(len(seq)):
		if seq[i] >= 10:
			seq[i] = alphabet[seq[i]]
		else: seq[i] = str(seq[i])
	seq = ''.join(seq)
	return seq
	
def transform_to_base10 (number, base_0):
	
	digits = num_to_list(number)
	to_return = 0
	
	for i in range(len(digits)):
		digit = digits.pop() * power(base_0, i)
		to_return += digit
	return str(to_return)

def transform_from_base10 (number, base_1):
	
	reminders = []
	devidend = int(number)
	reminder = 0
	
	while devidend != 0:
		reminder = devidend % base_1
		devidend = devidend // base_1
		reminders.append(reminder)
	number = list_to_num(reminders)
	return str(number)
	
	
while True: 
	
	variables = init_varibles()

	if variables["base_0"] != 10: 
		variables["number"] = transform_to_base10 (variables["number"], variables["base_0"])
	if variables["base_1"] != 10:
		variables["number"] = transform_from_base10(variables["number"], variables["base_1"])
	
	print ("То же число с новым основанием:", variables["number"], "\n")

