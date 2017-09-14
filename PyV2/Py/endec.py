
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Author: Rajagopal Senthil Kumar
    Created Date:  07-Sep-2017
    Modified Date: 07-Sep-2017
    Purpose: Internal library - Encryption and Decryption class 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class EnDec(object):

    def __init__(self, master_key): 
        self.master_key = hashlib.sha256(master_key.encode()).digest()
        self.block_size = 32
    
    def __padString(self, astring):
        return astring + (self.block_size - len(astring) % self.block_size) * chr(self.block_size - len(astring) % self.block_size)

    @staticmethod
    def __unpadString(astring):
        return astring[:-ord(astring[len(astring)-1:])]

    def encryptString(self, clear_text):
        clear_text = self.__padString(clear_text)
        secret_value = Random.new().read(AES.block_size)
        cipher_value = AES.new(self.master_key, AES.MODE_CBC, secret_value)
        encrypted_text=base64.b64encode(secret_value + cipher_value.encrypt(clear_text))
        return encrypted_text

    def decryptString(self, encrypted_text):
        encrypted_text = base64.b64decode(encrypted_text)
        secret_value = encrypted_text[:AES.block_size]
        cipher_value = AES.new(self.master_key, AES.MODE_CBC, secret_value)
        clear_text=self.__unpadString(cipher_value.decrypt(encrypted_text[AES.block_size:])).decode('utf-8')
        return clear_text

######## End of Encryption and Decryption Program########################################################## 



