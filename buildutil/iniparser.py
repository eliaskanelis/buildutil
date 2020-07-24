#!/usr/bin/env python3


import configparser
import os


class IniParser():

	def __init__(self, iniPathFile=None):
		self.iniPathFile = iniPathFile
		ini = configparser.ConfigParser()
		ini.optionxform = str
		ini.read(self.iniPathFile)

		# Create directory if it does not exist
		iniDirpath = os.path.dirname(self.iniPathFile)
		if os.path.isdir(iniDirpath) is False:
			os.makedirs(iniDirpath)

		# Create ini file if it does not exist
		try:
			with open(self.iniPathFile, 'w') as configfile:
				ini.write(configfile)
		except:
			raise Exception(f"Could not create '{self.iniPathFile}'")


	def read(self, section, key):
		# Read ini file
		ini = configparser.ConfigParser()
		ini.optionxform = str
		ini.read(self.iniPathFile)

		# Validate
		#if section == "" or section is None:
		#	section = "DEFAULT"
		#if section == None or section == "DEFAULT":
		#	section = None

		if key == "" or key is None:
			return

		# Get configuration
		rv = None
		try:
			rv = ini[section][key]
			#rv = ini.get(section, key)
		except Exception as e:
			#raise(e)
			#print(f"{section} {key}")
			rv = None


		# Translate value
		if rv == "True":
			rv = True
		elif rv == "False":
			rv = False
		#elif rv == "None":
		#	rv = None
		else:
			try:
				return int(rv)
			except Exception:
				pass

			try:
				return float(rv)
			except Exception:
				pass

		return rv


	def write(self, section, key, value, update=True):

		# Read ini file
		ini = configparser.ConfigParser()
		ini.optionxform = str
		ini.read(self.iniPathFile)

		# Validate
		if section == "" or section is None:
			return

		if key == "" or key is None:
			return

		# No need to write file when file value equals the new value
		rv = self.read(section, key)
		if value == rv:
			return

		# Update
		if update is False and rv != None:
			return

		# Prepare value
		if value is None:
			return
		value = str(value)

		# Set configuration
		if ini.has_section(section) is False and section != "DEFAULT":
			ini.add_section(section)

		try:
			ini.set(section, key, value)
		except:
			raise Exception(f"Could not write [{section}][{key}] = {value}")

		# Write ini file
		try:
			with open(self.iniPathFile, 'w') as configfile:
				ini.write(configfile)
		except:
			raise Exception(f"Could not write to '{self.iniPathFile}'")

		#print(f"Wrote: [{section_key}] = '{value}")

	def __str__(self):
		rv = ""
		try:
			with open(self.iniPathFile, 'r') as configfile:
				rv = configfile.read()
		except:
			raise Exception(f"Could read to '{self.iniPathFile}'")

		return rv


def main():

	iniFilepath = "/tmp/test.ini"

	# Create ini parser
	parser = IniParser(iniFilepath)

	# Write
	section = "section"
	key = "key"
	value = "value"
	parser.write(section, key, value, update=False)

	# Read back
	rv = parser.read(section, key)

	# Validate and see results
	print(parser)
	if rv != value:
		raise Exception("FAILLURE!!")

	# Delete ini file
	import os
	if os.path.exists(iniFilepath):
		os.remove(iniFilepath)


if __name__ == "__main__":
	main()
