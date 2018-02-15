from ciphers import Cipher

# Functions retreived from https://github.com/Lellansin/Cipher-examples/tree/master/python
class Affine(Cipher):
    DIE = 128;

    KEY = (7, 3, 55)

    def __init__(self):
        pass

    def encryptChar(self, char):
        K1, K2, kI = self.KEY
        return chr((K1 * ord(char) + K2) % self.DIE)

    def encrypt(self, string):
        return "".join(map(self.encryptChar, string))

    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        return chr(KI * (ord(char) - K2) % self.DIE)

    def decrypt(self, string):
        return "".join(map(self.decryptChar, string))