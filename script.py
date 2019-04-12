__author__ = "Akshay Parakh"

import sys

filename = sys.argv[1]

def is_legal(word):
	for chr in word:
		if chr.isalpha() or chr.isdigit() or chr == '\'' or chr == '-':
			pass
		else:
			word = word.replace(chr, '')
	return word

if __name__ == '__main__':
	file = open(filename, 'r')
	content = file.read()
#	print(content)
	content = content.split()
	file.close()

	word_list = list()
	for item in content:
		word = is_legal(item)
		if len(word):
			word_list.append(word)
#	print(word_list)

	word_count = dict()
	for word in word_list:
		if word.lower() not in word_count.keys():
			word_count[word.lower()] = 1
		else:
			word_count[word.lower()] += 1
#	print(word_count)
	sorted_val = sorted(word_count.items(), key = lambda kv: (-kv[1], kv[0]))
	with open("freq.txt", "w+") as outfile:
		for pair in sorted_val:
			outfile.write(str(pair)+'\n')
	sorted_key = sorted(word_count.items(), key = lambda kv: kv[0])
	with open("alphabhatical.txt", "w+") as outfile:
		for pair in sorted_key:
			outfile.write(str(pair)+'\n')
#	print(sorted_key)
	
