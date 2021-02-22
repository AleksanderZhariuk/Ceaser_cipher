import os
from caesar_art import logo


def caesar_rus(user_text, shift_amount, encode_or_decode):
	if encode_or_decode == 'encode':
		encrypt_word = ''
		for letter in user_text:
			if letter == ' ' or letter in symbols_and_numbers:
				encrypt_word += letter
			elif letter in eng_alphabet:
				encrypt_letter_index = eng_alphabet.index(letter) + shift_amount
				if encrypt_letter_index > len(eng_alphabet) - 1:
					encrypt_letter_index -= len(eng_alphabet)
				encrypt_word += eng_alphabet[encrypt_letter_index]
			else:
				encrypt_letter_index = alphabet.index(letter) + shift_amount
				if encrypt_letter_index > len(alphabet) - 1:
					encrypt_letter_index -= len(alphabet)
				encrypt_word += alphabet[encrypt_letter_index]
		print(f'Зашифрованное предложение: {encrypt_word.capitalize()}')
	elif encode_or_decode == 'decode':
		decrypt_word = ''
		for letter in user_text:
			if letter == ' ' or letter in symbols_and_numbers:
				decrypt_word += letter
			elif letter in eng_alphabet:
				decrypt_letter_index = eng_alphabet.index(letter) - shift_amount
				while decrypt_letter_index < 0:
					decrypt_letter_index = len(eng_alphabet) + decrypt_letter_index
				decrypt_word += eng_alphabet[decrypt_letter_index]
			else:
				decrypt_letter_index = alphabet.index(letter) - shift_amount
				while decrypt_letter_index < 0:
					decrypt_letter_index = len(alphabet) + decrypt_letter_index
				decrypt_word += alphabet[decrypt_letter_index]
		print(f'Расшифрованное предложение: {decrypt_word.capitalize()}')



def caesar_eng(user_text, shift_amount, encode_or_decode):
	if encode_or_decode == 'encode':
		encrypt_word = ''
		for letter in user_text:
			if letter == ' ' or letter in symbols_and_numbers:
				encrypt_word += letter
			else:
				encrypt_letter_index = eng_alphabet.index(letter) + shift_amount
				if encrypt_letter_index > len(eng_alphabet) - 1:
					encrypt_letter_index -= len(eng_alphabet)
				encrypt_word += eng_alphabet[encrypt_letter_index]
		print(f'The encoded text is {encrypt_word.capitalize()}')
	elif encode_or_decode == 'decode':
		decrypt_word = ''
		for letter in user_text:
			if letter == ' ' or letter in symbols_and_numbers:
				decrypt_word += letter
			else:
				decrypt_letter_index = eng_alphabet.index(letter) - shift_amount
				while decrypt_letter_index < 0:
					decrypt_letter_index = len(eng_alphabet) + decrypt_letter_index
				decrypt_word += eng_alphabet[decrypt_letter_index]
		print(f'The decoded text is {decrypt_word.capitalize()}')



russian_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
symbols_and_numbers = "!,;?.#%@^%:№*()-+=$&1234567890"
alphabet = []
eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in russian_letters:
	alphabet.append(letter)

print(logo)
language = input('Choose your language [RU/ENG]: ').lower()
repeat = 'y'

if language == 'ru':
	while repeat == 'y':
		os.system('cls' if os.name == 'nt' else 'clear')
		user_choice = input("Выберите, что требуется. Для зашифровки сообщения напишите 'encode'. Если же вы хотите расшифровать сообщение напишите 'decode'.\n").lower()
		print('-' * 60)
		if user_choice == 'encode' or user_choice == 'decode':
			text = input('Введите текст:\n').lower()
			print('-' * 60)
			shift = int(input('Смещение:\n'))
			shift = shift % len(alphabet)
			print('-' * 60)
			caesar_rus(user_text=text, shift_amount=shift, encode_or_decode=user_choice)
		else:
			print("Неизвестная команда!")
		repeat = input("Желаете повторить? [Y/N]").lower()
	os.system('cls' if os.name == 'nt' else 'clear')
elif language == 'eng':
	while repeat == 'y':
		os.system('cls' if os.name == 'nt' else 'clear')
		user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
		print('-' * 60)
		if user_choice == 'encode' or user_choice == 'decode':
			text = input('Type your message:\n').lower()
			print('-' * 60)
			shift = int(input('Type the shift number:\n'))
			shift = shift % len(eng_alphabet)
			print('-' * 60)
			caesar_eng(user_text=text, shift_amount=shift, encode_or_decode=user_choice)
		else:
			print('Incorrect command!')
		repeat = input('Do you want to repeat? [Y/N]').lower()
	os.system('cls' if os.name == 'nt' else 'clear')
else:
	print("I don't know this language :)")

