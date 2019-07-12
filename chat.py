def read_file(filename):
	data = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			data.append(line.strip())
	return data


def convert(data):
	output = []
	person = None
	for d in data:
		if d == 'Allen' or d == 'Tom':
			person = d
			continue
		else:
			if person:
				output.append(person + ':' + d)
	return output


def write_file(filename, output, encoding='utf-8'):
	with open(filename, 'w') as f:
		for out in output:
			f.write(out + '\n')

def main():
	data = read_file('input.txt')
	output = convert(data)
	write_file('output.txt', output)

main()