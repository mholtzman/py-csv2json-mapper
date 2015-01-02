from modules import mapper
import json, sys

# constants, make these configurable via options
FIELD_SEPARATOR = ','
SCHEMA_DELIM = '.'

if len(sys.argv) != 3:
	print("You must provide an input and output file! Usage: csv2json.py <inputfile> <outputfile>")
	sys.exit()
	
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

with open(input_file_path, 'r') as input_file:
	lines = input_file.read().splitlines()

	# the first line is the schema for the entire file
	schema = lines[0].split(FIELD_SEPARATOR)
	data = []

	for row in lines[1:]:
		data.append(mapper.parse_row(schema, row.split(FIELD_SEPARATOR), SCHEMA_DELIM))
		
	with open(output_file_path, 'w') as output_file:
		output_file.write(json.dumps(data, indent=2))
	
	if output_file.closed:
		print("All data successfully mapped!")
	else:
		print("An error occurred, please check your data and schema!")