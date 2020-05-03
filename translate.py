import sys

input = input()

result = ""

f = open ("en-es.tsv", "r")

trap = {}

for line in f.readlines():
	if len(line) > 2:
		trap[line.split()[1]] = line.split()[2]

for word in input.split():
	if word in trap:
		result += trap[word] + " "
	else:
		result += word + "* "

print(result)
