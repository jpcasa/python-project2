# coding=utf-8
# Retrieved from https://github.com/nboubakr/polybius-square/blob/master/polybius.py

import os
from ciphers import Cipher

class Polybius(Cipher):

    def __init__(self):
        pass

    def __prepare_sentence__(self, sentence):
		"""Prepare a sentence for the encryption"""
		accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
		ascii = ["A", "E", "I", "O", "U", "C"]

		i = 0
		for word in accent: # Replacing accented characters possible
			for letter in word:
				sentence = sentence.replace(letter, ascii[i])
			i += 1
		for letter in "',-;:!?.":  # Remove punctuation
			sentence = sentence.replace(letter, "")
		sentence = sentence.upper()  # Passage in capitals letters
		return sentence

    def encrypt(self, to_encrypt):
        List_H, List_V, message = [], [], ""
        for j in range(4):
            for i in range(5):
                List_H.append(chr(65+5*j+i))
            List_V.append(List_H)
            List_H = []
        List_H = []
        List_H.append(chr(85))
        List_H.append(chr(86))
        List_H.append(chr(88))
        List_H.append(chr(89))
        List_H.append(chr(90))
        List_V.append(List_H)

        to_encrypt = self.__prepare_sentence__(to_encrypt)
        to_encrypt = to_encrypt.replace(" ", "")

        for i in range(len(to_encrypt)):
            pos = ord(to_encrypt[i])-65
            verti = str(int((pos/5)+1))
            hori = str((pos % 5)+1)
            message += verti + hori + " "

        return message

    def decrypt(self, to_decrypt):
        List_H, List_V, message = [], [], ""
        for j in range(4):
            for i in range(5):
                List_H.append(chr(65+5*j+i))
            List_V.append(List_H)
            List_H = []
        List_H = []
        List_H.append(chr(85))
        List_H.append(chr(86))
        List_H.append(chr(88))
        List_H.append(chr(89))
        List_H.append(chr(90))
        List_V.append(List_H)

        to_decrypt = to_decrypt.replace(" ", "")
        length = len(to_decrypt)

        for h in range(0, length, 2):
            pos = int(to_decrypt[h])-1
            pos2 = int(to_decrypt[h+1])-1
            message += List_V[pos][pos2]

        return message
