
# packages required for encryption and encodings


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Author: Rajagopal Senthil Kumar
    Created Date:  07-Sep-2017
    Modified Date: 07-Sep-2017
    Purpose: Internal library - maintain key data elements and root class of program 360 library

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



class Internal(object):

    __author="Rajagopal senthil kumar, sendakil@yahoo.com"
    __version="01.00.00"
    __sqldb_password=b'i+Z0OJimdumhvtbxzKEXZgox6e2FxZBiSLY+pAfgwb/4lJcPsgbL0RVMTLjzVRdA'
    __encryption_masterkey="123456789012345####"


    def __init__(self):
        pass

    def getVersion(self):
        return self.__version

    def getAuthor(self):
        return self.__author  

    def getMasterKey(self):
        return self.__encryption_masterkey

    def getSQLPassword(self):
         return self.__sqldb_password


       

    


#End of this Program#########################################################################################################

