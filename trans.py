# -*- coding: utf-8 -*-
#
# Transposition Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

# 
# 置换
# 
def transposition(matrix, words):
    cipher = ''
    length = len(matrix)
    blanks = ''.join(' ' for i in range(length - 1))

    for x in range(0, len(words), length):
        # todo 优化
        item = words[ x : x + length ] + blanks
        for pos in matrix:
            cipher += item[pos - 1]

    return cipher.lower()


def reverse(matrix):
    length = len(matrix)
    arr = [0] * length
    for i in range(length):
        arr[matrix[i] - 1] = i + 1
    return arr


if __name__ == '__main__':

    text = 'Informationsecurityisimportant';
    matrix = [2, 4, 1, 3]
    print('strmatrix:  ' + str(matrix))
    
    ciphertext = transposition(matrix, text)
    print('encrypted: ' + ciphertext)
    secret = reverse(matrix)
    print('decrypted: ' + str(secret))
    print('secret: ' + transposition(secret, ciphertext))