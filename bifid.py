from ciphers import Cipher
from polybius import Polybius

# Functions retreived from https://github.com/Lellansin/Cipher-examples/tree/master/python
class Bifid(Cipher):

	def __init__(self):
		self.poly = Polybius()
		self.table = [['B', 'G', 'W', 'K', 'Z'], ['Q', 'P', 'N', 'D', 'S'], ['I', 'O', 'A', 'X', 'E'], ['F', 'C', 'L', 'U', 'M'], ['T', 'H', 'Y', 'V', 'R']]

	# Encryption
	def encrypt(self, text):
	    string = self.table
	    cipher_row, cipher_col = '', ''
	    for ch in text.upper():
	        for row in range(len(self.table)):
	            if ch in self.table[row]:
	                cipher_row += str(row + 1)
	                cipher_col += str((self.table[row].index(ch) + 1))
	    return self.poly.decrypt(cipher_row + cipher_col)

	# Decryption
	def decrypt(self, text):
	    numbers = ''
	    text = self.poly.encrypt(text)
	    a, b = text[:len(text) / 2], text[len(text) / 2:]
	    numbers = ''.join(a[i] + b[i] for i in range(len(a)))
	    return self.poly.decrypt(numbers)