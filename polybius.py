import random
from ciphers import Cipher

# Functions retreived from https://github.com/Lellansin/Cipher-examples/tree/master/python
class Polybius(Cipher):

	def __init__(self):
		self.table = self.generate_table()

	# Generates a random number
	def rand(self, min, max):
		return int((max - min) * random.random() + min)

	# Generates the Table
	def generate_table(self, size = 5):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		table = [[0] * size for row in range(size)]

		for y in range(size):
			for x in range(size):
				table[x][y] = alphabet[self.rand(0, len(alphabet))]
				alphabet = alphabet.replace(table[x][y], '')
		return table

	# Encryption
	def encrypt(self, words):
		string = self.table
		cipher = ''
		for ch in words:
			for row in range(len(self.table)):
				if ch in self.table[row]:
					x = str((self.table[row].index(ch) + 1))
					y = str(row + 1)
					cipher += y + x
		return cipher

	# Decryption
	def decrypt(self, numbers):
		text = ''
		for index in range(0, len(numbers), 2):
			y = int(numbers[index]) - 1
			x = int(numbers[index + 1]) - 1
			text += self.table[y][x]
		return text