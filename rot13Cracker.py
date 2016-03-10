import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits

def shift(cipher, key):
    text = ""
  
    for sel in cipher:
        search_space = DIGITS
        if sel in LOWER:
            search_space = LOWER
        elif sel in UPPER:
            search_space = UPPER

        for index, char in enumerate(search_space):
            if char == sel:
                shift_count = index - key
                while shift_count >= len(search_space):
                    shift_count = (key - len(search_space))
    
                text += search_space[shift_count]
                break

    return text
  
  

cipher_text = input("Enter Cipher Text: ")
key = int(input("Enter Numeric Key: "))
plain_text = shift(cipher_text, key)
print("Plain Text: \n" + plain_text)
