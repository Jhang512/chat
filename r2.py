def read_file(filename):
	data = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			data.append(line.strip())
	return data


def count(data):

	allen_pic = 0
	allen_word = 0
	allen_sticker = 0

	viki_pic = 0
	viki_word = 0
	viki_sticker = 0

	for d in data:
		text = d.split(' ')

		time = text[0]
		name = text[1]

		if name== 'Allen':
			if text[2] == '貼圖':
				allen_sticker += 1
			elif text[2] == '圖片':
				allen_pic += 1
			else:
				for m in text[2:]:
					allen_word += len(m)
		elif name == 'Viki':
			if text[2] == '貼圖':
				viki_sticker += 1
			elif text[2] == '圖片':
				viki_pic += 1
			else:
				for m in text[2:]:
					viki_word += len(m)

	print('allen_pic : ', allen_pic)
	print('allen_word : ', allen_word)
	print('allen_sticker : ', allen_sticker)

	print('viki_pic : ', viki_pic)
	print('viki_word : ', viki_word)
	print('viki_sticker : ', viki_sticker)


def write_file(filename, output, encoding='utf-8'):
	with open(filename, 'w') as f:
		for out in output:
			f.write(out + '\n')

def main():
	data = read_file('-LINE-Viki.txt')
	count(data)
	# write_file('output.txt', output)

main()