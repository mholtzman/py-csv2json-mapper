from modules import mapper
import json

FIELD_SEPARATOR = ','
SCHEMA_DELIM = '.'

with open('test-data.csv', 'r') as input_file:
	lines = input_file.read().splitlines()

	# the first line is the schema for the entire file
	schema = lines[0].split(FIELD_SEPARATOR)
	data = []

	for row in lines[1:]:
		data.append(mapper.parse_row(schema, row.split(FIELD_SEPARATOR), SCHEMA_DELIM))
		
	with open('parsed_output.json', 'w') as output_file:
		output_file.write(json.dumps(data, indent=2))
	
	if output_file.closed:
		print("All data successfully mapped!")
	else:
		print("An error occurred, please check your data and schema!")