import os
import sys

STDOUT_FILENO = 1

ERROR = 0
SIMPLE = 1
REDIRECT = 2
PIPE = 3
SET_VAR = 4
SHELL_EXIT = 5

MAX_ARGS = 8

EXIT_SUCCESS = 0

env_variable_value = None
env_variable_name = None
out_file = None
args = []


# @filedes  - file descriptor to be redirected
# @filename - filename used for redirection
def do_redirect(filedes, filename):
	# TODO 3 - Redirect filedes into fd representing filename (Hint: dup2)
	pass

	
def set_var():
	# TODO 2 - Set the environment variable

def expand(name):
	# TODO 2 - Return the value of environment variables

#  @args - array that contains a simple command with parrameters
def simple_cmd(args):
	# TODO 1 - Create a process to execute the command */
	try:
		
		pid = os.fork ()
		if pid == -1:
            # TODO 1 - error
			pass
		elif pid == 0:
		    # redirect standard output if needed */
			if out_file != None:
				# print ("out file")

		    # TODO 1 - child process 
			# please note args is a list of strings:
			# args[0] - is the command
			# args[1] - the first parameter
			# args[2] ....
			# Hint: use one of the execv... functions (Hint: man exec)


		else:
		    # TODO 1 -  parent process
			pass

	except Exception as e:
		print ("Error: {}".format (e))

def parse_line (line):

	global env_variable_value
	global env_variable_name
	global out_file
	global args
	global value
	out_file = None
	env_variable_value = None
	env_variable_name = None
	args = []
	ret = SIMPLE

	# check for exit
	if line == "exit":
		return SHELL_EXIT

	# var = value
	if '=' in line:
		tokens = line.split ('=')
		if len(tokens) != 2:
			return ERROR

        # get var; make sure line is correct
		var_tokens = tokens[0].split ()
		if len(var_tokens) != 1:
			return ERROR
		env_variable_name = var_tokens[0]
        # get value; make sure line is correct
		value_tokens = tokens[1].split ()
		if len(value_tokens) != 1:
			return ERROR
		env_variable_value = value_tokens[0]
		return SET_VAR

	# normal command 
	# copy args
	tokens = line.split()

	redirect = False
	for index,token in enumerate(tokens):
		if token[0] == '$':
			new_token = expand (token[1:])
			if new_token == None:
				print(" Expansion failed")
				return ERROR
			args.append (new_token)
		elif token == ">":
			out_file = tokens[index+1]
			redirect = True
		else:
			if not redirect:
				args.append (token)
			else:
				redirect = False
	return ret

def main ():
	while True:
		line = input("> ")

		cmd_type = parse_line(line)

		# print ("cmd_type: {}".format (cmd_type))
		# print (args)

		if cmd_type == SHELL_EXIT:
			sys.exit(EXIT_SUCCESS)
		elif cmd_type == SET_VAR:
			set_var()
		elif cmd_type == SIMPLE:
			simple_cmd(args)

main()
