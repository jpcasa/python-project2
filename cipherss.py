# class Ciphers:

# 	def __init__(self):
# 		self.table = ""

# 	def encrypt(self):
# 		raise NotImplementedError()

# 	def decrypt(self):
# 		raise NotImplementedError()

# 	def rand(self, min, max):
# 		return ''

# 	def generate_table(self):
# 		alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
#     	table = [[0] * 5 for row in range(5)]
#     	for y in range(5):
#     		table[x][y] = alphabet[rand(0, len(alphabet))]
#     		alphabet = alphabet.replace(table[x][y], '')
#     	return ''