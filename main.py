
import sys
import rsa

class Decrypt:
  def __init__(self):
    self.privateKey = input("Please enter your private key: ")
    self.publicKey = open("publicKey.txt", 'r').readline()
    self.message = open("message.txt", 'r').readline()
  def getString():
    return rsa.decrypt(self.message,self.privateKey).decode()
 
class Encrypt:
  def __init__(self):
    self.message = input("Please enter the message you want to store: ")
    publicKey,privateKey = rsa.newkeys(256)
    self.publicKey=publicKey;
    self.privateKey=privateKey;
    
    print("Your private key is used to decrypt the string, store it somewhere safe, \n ---------------Begin RSA Private Key \n {} \n ---------------------End RSA Private Key \n")
    open("publicKey.txt", "a").write(self.publicKey).close()
    open("message.txt", "a").write(rsa.encrypt(messsage.encode(),self.publicKey)).close()
    

# CLI
cli_type = sys.argv[1]
if cli_type == 'encrypt':
  Encrypt()
elif cli_type == 'decrypt':
  Decrypt()
else:
  print("Usage:: \n\t python3 main.py <OPT ENCRYPT||DECRYPT>")
