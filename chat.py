def read_file(filename):
	data = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			data.append(line)
	return data


def transform(data):
	output = []
	for d in data:
		if 'Allen' in d or 'Tom' in d:
			speaker = d
			continue
		else:
			output.append(speaker + ':' + d)
	return output


def write_file(filename, output):
	with open(filename, 'w') as f:
		for out in output:
			f.write(out + '\n')


data = read_file('input.txt')
output = transform(data)
write_file('output.txt', output)