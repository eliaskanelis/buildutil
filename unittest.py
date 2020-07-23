#!/usr/bin/env python3

from buildutil.iniparser import IniParser

import pytest
import os

iniFilepath = "/tmp/test.ini"



# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

#def setup():
#	pass


#def cleanup():
#	# Delete ini file
#	if os.path.exists(iniFilepath):
#		os.remove(iniFilepath)

def test_fuck():
	assert 1 == 0
	assert True == False


def test_1():
	iniFilepath = "/tmp/test.ini"

	##########################################
	def check(section, key, value):
		parser = IniParser(iniFilepath)
		rv = parser.read(section, key)
		assert rv == value
		if rv == value:
			print(f"[SUCCESS]\t[{section}][{key}]: '{rv}'")
		else:
			print(f"[FAIL   ]\t[{section}][{key}]: '{rv}'\t\tExpected: '{value}'")

	testArray = [
		#[None, "Invalid1", "True"  ],
		#[None, "Invalid2", "False" ],
		["DEFAULT",  "String",   "Hello" ],
		["DEFAULT",  "True",     True    ],
		["DEFAULT",  "False",    False   ],
		["DEFAULT",  "Int",      1       ],
		["DEFAULT",  "Float",    3.14    ],
		["DEFAULT",  "None",     None    ]
	]

	# Write
	for line in testArray:
		if len(line) == 3:
			section     = line[0]
			key         = line[1]
			value       = line[2]
			parser = IniParser(iniFilepath)
			parser.write(section, key, value, update=False)

	# Check
	for line in testArray:
		if len(line) == 3:
			section     = line[0]
			key         = line[1]
			value       = line[2]
			if section is None:
				section = "DEFAULT"
			check(section, key, value)

	##########################################
	# Check
	parser.write("UPDATE", "test", "Original", update=False)
	check("UPDATE", "test", "Original")
	parser.write("UPDATE", "test", "Updated",  update=False)
	check("UPDATE", "test", "Original")

	##########################################
	# Delete ini file

	#print(parser)
	import os
	if os.path.exists(iniFilepath):
		os.remove(iniFilepath)



def main():
	#print("Hello")
	#test1()
	test_fuck()

if __name__ == "__main__":
	main()
