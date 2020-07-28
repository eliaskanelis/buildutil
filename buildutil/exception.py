#!/usr/bin/env python3


from invoke.exceptions import Exit


class ConfigError(Exit):
	def __init__(self, message):
		# Call the base class constructor with the parameters it needs
		super(ConfigError, self).__init__("\033[31;1;1mERROR:\033[0m " + message)
