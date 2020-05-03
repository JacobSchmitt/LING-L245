import sys

#this spellechecker is for Spanish

fd = open('wiki.hist', 'r')
reference = []
for line in fd.readlines():
        if line.strip().count(' ') == 0:
                continue
        line = line.strip()
        (f, w) = line.split(' ')
        reference.append(w)

text = sys.stdin.read()
input = text.split()

result = ""

for i in range (0, len(input)):
        if input[i] in reference:
                result += input[i] + " "
        else:
                result += input[i] + "* "
