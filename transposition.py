from ciphers import Cipher

# Functions retreived from https://github.com/Lellansin/Cipher-examples/tree/master/python
class Transposition(Cipher):

	def __init__(self):
		self.matrix = [2, 4, 1, 3]

	# Encryption
	def encrypt(self, words):
		cipher = ''
		length = len(self.matrix)
		blanks = ''.join(' ' for i in range(length - 1))

		for x in range(0, len(words), length):
			item = words[ x : x + length ] + blanks
			for pos in self.matrix:
				cipher += item[pos - 1]

		return cipher.lower()

	# Decryption
	def decrypt(self, words):
		length = len(self.matrix)
		arr = [0] * length
		for i in range(length):
			arr[self.matrix[i] - 1] = i + 1
		return arr