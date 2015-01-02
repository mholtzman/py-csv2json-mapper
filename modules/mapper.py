def parse_row(schema, data, schema_delim):
	root = {}
	
	for entry, value in zip(schema, data):
		parse_schema_entry(root, entry.split(schema_delim), value)
		
	return root
		
def parse_schema_entry(node, entry, data):
	next_child = entry[0]
	
	if len(entry) == 1:
		# if this is a leaf, add the data
		node[next_child] = data
	else:	
		# if this is not a leaf, recursively process the rest of the entry
		if not next_child in node:
			node[next_child] = {}
			
		parse_schema_entry(node[next_child], entry[1:], data)