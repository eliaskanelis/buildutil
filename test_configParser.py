#!/usr/bin/env python3

from buildutil.configParser import ConfigParser
from buildutil.configParser import array2Dict

import os
import pytest


iniFilepath = "/tmp/buildutil/test.ini"


def cleanup():
	# Make sure the inifile is removed before the test
	if os.path.exists(iniFilepath):
		os.remove(iniFilepath)
	assert os.path.exists(iniFilepath) is False


def check(section, key, expected_value):
	value = os.environ.get(key)
	assert value == expected_value


############################################################


def test_noDefaultsArgGiven():

	cleanup()

	ConfigParser(iniFilepath)

	assert os.path.exists(iniFilepath) is False
	cleanup()


def test_NoneDefaultsGiven():

	cleanup()

	ConfigParser(iniFilepath, None)

	assert os.path.exists(iniFilepath) is False
	cleanup()


def test_noIniFilepathGiven():

	cleanup()

	with pytest.raises(Exception):
		ConfigParser(None)

	assert os.path.exists(iniFilepath) is False
	cleanup()


def test_readDefaults():

	cleanup()

	lst = array2Dict([
		# Section Key Default Options
		["MAKE", "PORT", "posix", {"posix", "stm32f072rb"}],
		["MAKE", "TARGET", "dbg", {"dbg", "rel"}],
		["MAKE", "test", "dbg", {"dbg", "rel"}],
	])

	parser = ConfigParser(iniFilepath, lst)
	parser.setenv()

	for d in lst:
		section = d["section"]
		key = d["key"]
		expected_value = d["default"]
		check(section, key, expected_value)

	cleanup()


def test_types():

	cleanup()

	lst = array2Dict([
		# Section Key Default Options
		["MAKE", "PORT", "posix", {"posix", "stm32f072rb"}],
		["MAKE", "TARGET", "True", {"True", "False"}],
		# ["MAKE", "test", True, {True, False}],
	])

	parser = ConfigParser(iniFilepath, lst)
	parser.setenv()

	for d in lst:
		section = d["section"]
		key = d["key"]
		expected_value = d["default"]
		check(section, key, expected_value)

	cleanup()


def test_writeRead():

	cleanup()

	parser = ConfigParser(iniFilepath)

	parser.write("SECTION", "TEST", "Hello")
	rv = parser.read("SECTION", "TEST")
	assert rv == "Hello"

	cleanup()


def test_readSomethingNotWritten():

	cleanup()

	parser = ConfigParser(iniFilepath)

	rv = parser.read("SECTION", "TEST")
	assert rv is None

	cleanup()


def test_overWriteDefaultWithValid():

	cleanup()

	lst = array2Dict([
		# Section    Key      Default  Options
		["MAKE", "PORT", "posix", {"posix", "stm32f072rb"}]
	])

	parser = ConfigParser(iniFilepath, lst)

	# Read default
	rv = parser.read("MAKE", "PORT")
	assert rv == "posix"

	# Overwrite default
	parser.write("MAKE", "PORT", "stm32f072rb")

	# Check
	rv = parser.read("MAKE", "PORT")
	assert rv == "stm32f072rb"

	cleanup()


def test_overWriteDefaultWithInvalid():

	cleanup()

	lst = array2Dict([
		# Section    Key      Default  Options
		["MAKE", "PORT", "posix", {"posix", "stm32f072rb"}]
	])

	parser = ConfigParser(iniFilepath, lst)

	# Read default
	rv = parser.read("MAKE", "PORT")
	assert rv == "posix"

	# Overwrite default
	with pytest.raises(Exception):
		parser.write("MAKE", "PORT", "new")

	# Check that old value is still there
	rv = parser.read("MAKE", "PORT")
	assert rv == "posix"

	cleanup()


def main():
	pass


if __name__ == "__main__":
	main()
