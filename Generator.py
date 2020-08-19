from os import system, path
import sys
from itertools import product

#------------------------------------------------------------------------------------------------------

if(path.isfile('alphabet.txt')):
	file_in = open('alphabet.txt','r')
else:
	print('Конфиг с названием alphabet.txt отсутствует! Он создан автоматически!')
	file = open('alphabet.txt','w')
	file.write('consonants:\n')
	file.write('\n')
	file.write('vowels:\n')
	file.close()
	input('Нажмите Enter для завершения программы!')
	sys.exit()

#------------------------------------------------------------------------------------------------------

consonants = [] #согласные
vowels = [] #гласные
flag = False
for line in file_in:
	line = line.replace('\n','')
	line = line.lower()
	if(line == 'vowels:'):
		flag = True
	if(line != 'consonants:' and not flag):
		consonants.append(line)
	if(line != 'vowels:' and flag):
		vowels.append(line)

if(len(consonants) + len(vowels) == 0):
	print('Конфиг с названием alphabet.txt пуст!')
	file_in.close()
	input('Нажмите Enter для завершения программы!')
	sys.exit()

#------------------------------------------------------------------------------------------------------

while(True):
	length = input('Введите длину слов: ')
	if(length.isdigit()):
		length = int(length)
		break
	else:
		print('Это не число, попробуйте ещё раз!')

#------------------------------------------------------------------------------------------------------

letters = []
flag = False
print('Введите буквы:')
while(True):
	f = False
	f1 = True
	a = str(input()).lower()
	if(a == ''):
		if(flag):
			break
		else:
			print('Вы хотите закончить ввод? Если да, то вновь нажмите Enter')
			flag = True
	else:
		for consonant in consonants:
			if(a == consonant):
				f = True
				break
		for vowel in vowels:
			if(a == vowel):
				f = True
				break
		if(f):
			for letter in letters:
				if(a == letter):
					f1 = False
					print('Данная буква уже была введена!')
					break
			if(f1):
				letters.append(a)
		else: 
			print('Буква отсутствует в конфиге!')
		flag = False

#------------------------------------------------------------------------------------------------------

input('Нажмите Enter, чтобы продолжить')
system('cls')
patterns = []
flag = False
print('Введите паттерны (c - согласные, v - гласные):')
while(True):
	a = str(input()).lower()
	if(a == ''):
		if(flag):
			break
		else:
			print('Вы хотите закончить ввод? Если да, то вновь нажмите Enter')
			flag = True
	else:
		if(len(a) != length):
			print('Внимание! Длина паттерна не равнозначна длине слов! Этот паттерн не будет записан!')
			flag = False
		else:
			patterns.append(a)
			flag = False

#------------------------------------------------------------------------------------------------------

input('Нажмите Enter, чтобы продолжить')
system('cls')
words = []
lines = []
file_out = open('words.txt', 'w')
ranges = []

if(len(patterns) != 0):
	for pattern in patterns:
		for p in pattern:
			if(p == 'c'):
				ranges.append(consonants)
			if(p == 'v'):
				ranges.append(vowels)

else:
	alphabet = consonants + vowels
	ranges = [alphabet for l in range(length)]

#------------------------------------------------------------------------------------------------------

for line in product(*ranges):
	lines.append(line)
for word in lines:
	words.append(''.join(word))
for word in words:
	file_out.write(word + '\n')

print('Слова составлены и были выведены в файл words.txt!\nВсего слов:', len(words))

file_out.close()

input('Нажмите Enter для завершения программы!')