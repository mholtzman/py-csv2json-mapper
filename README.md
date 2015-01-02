py-csv2json-mapper
==================
This is a simple utility that takes a flat CSV file and transforms it into a JSON file.

Syntax
------

`python csv2json.py input_filename output_filename`

***

The first row of the CSV represents the JSON schema. Each column is the path to a leaf node and must represent the path to the given node separated by a configurable delimiter. The mapper will create nested objects as necessary so only the leaves (and hence, the data) need to be defined. Here's an example:

Desired JSON:
```json
"my_data": {
  "value1": "hello",
	"more_data": {
	  "value2": "goodbye"
	}
}
```

The CSV file to represent this would look as follows:
```
my_data.value1,my_data.more_data.value2
hello,goodbye
```