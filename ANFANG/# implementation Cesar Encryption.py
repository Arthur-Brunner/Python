# implementation Cesar Encryption
 
ALPHABET = [
    ' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
 
#this function do encryption
def encrypt()->str:
    result = ""
    klarText = input("\nplease enter Text to be encrypted:")
    key = input("please enter encryption Key:")
    key = int(key)
    for charecter in klarText:
        alphabet_index = ALPHABET.index(charecter)
        print(f"\n{charecter}")
        print(f" index position in kunde text for Alphabet is:" + str(alphabet_index))
        new_char_index = alphabet_index+key
        encryptedChar = ALPHABET[new_char_index]
        print(f"das ist encrypted:!!!!:   " + encryptedChar)
    return "it is encrypted from  " + klarText + "and Key:" + key
 
def decode()->str:
    cypherText = input("\nplease enter Text to be DECRYPTED!!:")
    key = input("please enter DECRYPTION KEY!!:")
    return "it is DECRYPTED  from  " + cypherText + "and Key:" + key
 
def main():
    result =""
    print("hello , i am cesar enc and dec app!")
    userChoice = input("if you want decrypt press d oder encrypt press e:")
 
    if(userChoice == "e"):
        result = encrypt()
    elif userChoice == "d":
        result = decode()
    else:
        result = "you must enter only e or d"
 
    print(result)
 
if __name__ == "__main__":
    main()
 