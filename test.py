import json

f = open('output_data.json') # output data of test input file 'input_data.json'
g = open('test_output_data.json') # already generated test output file
k = json.load(f)
l = json.load(g)
if k == l: # comparing results from both
	print('Test successful. Output data of test input file matches test output data.')
else:
	print("Output data of test input file doesn't match test output file.")
