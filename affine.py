from ciphers import Cipher

# Functions retreived from https://github.com/Lellansin/Cipher-examples/tree/master/python
class Affine(Cipher):

	def __init__(self):
		self.width = 26      
		self.ASC_A = ord('A')
		# text = 'AFFINECIPHER'
    	# key = [5, 8]

    # Encryption
	def encrypt(self, key, words):
	    return ''.join([self.shift(key, ch) for ch in words.upper()])

	# Decryption
	def decrypt(self, key, words):
	    a, b = self.modInverse(key[0], self.width), -key[1]
	    return ''.join([self.unshift([a, b], ch) for ch in words.upper()])

	def shift(self, key, ch):
	    if str.isalpha(ch):
	        offset = ord(ch) - self.ASC_A
	        return chr(((key[0] * offset + key[1]) % self.width) + self.ASC_A)
	    return ''

	def unshift(self, key, ch):
	    offset = ord(ch) - self.ASC_A
	    return chr(((key[0] * (offset + key[1])) % self.width) + self.ASC_A)

	def gcd(self, a, b):
	    while a != 0:
	        a, b = b % a, a
	    return b

	def modInverse(self, a, m):
	    if self.gcd(a, m) != 1:
	        print("Error:")
	        quit()
	    u1, u2, u3 = 1, 0, a
	    v1, v2, v3 = 0, 1, m
	    while v3 != 0:
	        q = u3 // v3
	        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
	    return u1 % m