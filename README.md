py-csv2json-mapper
==================
This is a simple utility that takes a flat CSV file and transforms it into a JSON file.

Syntax
------

`csv2json.py <input_filename> <output_filename>`

***

The first row of the CSV represents the JSON schema. Each column is the path to a leaf node and must represent the path to the given node separated by a configurable delimiter. 

The mapper will create nested objects as necessary so only the leaves (and hence, the data) need to be defined. In order to represent an array of values, use a semicolon(;) delimiter with the column.

Here's an example:

Desired JSON:
```json
"my_data": {
	"value1": "hello",
	"more_data": {
		"value2": "goodbye",
		"other_values": [
			"hello",
			"new",
			"world"
		]
	}
}
```

The CSV file to represent this would look as follows:
```
my_data.value1,my_data.more_data.value2,my_data.more_data.other_values
hello,goodbye,hello;new;world
```

Note that no ordering is preserved and thus the generated JSON will not necessarily be output in the same order as the columns in the input file.