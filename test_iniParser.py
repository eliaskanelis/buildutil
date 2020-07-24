#!/usr/bin/env python3

from buildutil.iniparser import IniParser

import os


iniFilepath = "/tmp/buildutil/test.ini"


def write(parser, testArray):
	for line in testArray:
		if len(line) == 3:
			section     = line[0]
			key         = line[1]
			value       = line[2]
			parser.write(section, key, value, update=False)


def check(parser, section, key, value):
	rv = parser.read(section, key)
	assert rv == value


def checkTestArray(parser, testArray, col):
	for line in testArray:
		len(line) == col
		if len(line) == col:
			section     = line[0]
			key         = line[1]
			value       = line[2]
			check(parser, section, key, value)


def start():
	assert os.path.exists(iniFilepath) == False
	parser = IniParser(iniFilepath)
	assert os.path.exists(iniFilepath) == True
	return parser


def cleanup():
	assert os.path.exists(iniFilepath) == True
	if os.path.exists(iniFilepath):
		os.remove(iniFilepath)
	assert os.path.exists(iniFilepath) == False




def test_types():

	col = 3
	testArray = [
		# Section    Key         Value
		["DEFAULT",  "String",   "Hello" ],
		["DEFAULT",  "True",     True    ],
		["DEFAULT",  "False",    False   ],
		["DEFAULT",  "Int",      1       ],
		["DEFAULT",  "Float",    3.14    ],
		["DEFAULT",  "None",     None    ]
	]

	parser = start()
	write(parser, testArray)
	checkTestArray(parser, testArray, col)
	cleanup()


def test_special():

	col = 3
	testArray = [
		# Section    Key       Value
		#["",         "String", "a1" ],
		#["DEFAULT",  "",       "b2" ],
		#["",         "",       "c3" ],
		#["DEFAULT",  None,     "d4" ],
		#[None,       "Float",  "e5" ]
		#[None,       None,     "f6" ]
	]

	#parser = start()
	#write(parser, testArray)
	#checkTestArray(parser, testArray, col)
	#cleanup(iniFilepath)


	parser = start()
	parser.write(None, "test", "out")
	#check(parser, "DEFAULT", "test", "out")
	cleanup()



def test_invalid():
	col = 3
	testArray = [
		# Section    Key         Value
		[None, "Invalid1", "True"  ],
		[None, "Invalid2", "False" ]
	]

	parser = start()
	write(parser, testArray)
	#checkTestArray(parser, testArray, col)
	cleanup()


def test_writeUpdate():
	parser = start()

	parser.write("UPDATE", "test", "Original", update=False)
	check(parser, "UPDATE", "test", "Original")

	parser.write("UPDATE", "test", "Updated",  update=False)
	check(parser, "UPDATE", "test", "Original")

	parser.write("UPDATE", "test", "Updated",  update=False)
	check(parser, "UPDATE", "test", "Original")

	cleanup()


def main():
	test_types()
	test_writeUpdate()


if __name__ == "__main__":
	main()
