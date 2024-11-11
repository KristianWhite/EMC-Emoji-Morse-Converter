

def main():
    message = "Alcala - Harzgai Rocky Hill"
    result = letter_to_emoji(message.upper())
    print (result)
    message = "😠 "
    result = emoji_to_letter(message)
    print (result)
    #message = input("User Code:")
    #encrypted_ms = letter_to_emoji(message)
    #print(encrypted_ms)

morse_dict = {'A': '😠', 'B': '😁', 'C': '🥶', 'D': '🥸', 'E': '😑', 'F': '😘', 'G': '😀', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'}

def letter_to_emoji(message):
    
    
    cipher=''
    
    for letter in message:
        if letter != '':
            
            cipher += morse_dict[letter] + ''
        else:
            cipher += ''
    return cipher

def emoji_to_letter(message):
    message += ' '
    
    decipher = ''
    citext = ''
    for letter in message:
        
        # checks for space
        if (letter != ' '):
            
            # counter to keep track of space
            i = 0
            
            # storing morse code of a single character
            citext += letter
            
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            
            # if i = 2 that indicates a new word
            if i == 2 :
                
                # adding space to separate words
                decipher += ' '
            else:
                
                # accessing the keys using their values (reverse of encryption)
                decipher += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
                citext = ''
                
    return decipher


def mode_switch():
    ...


if __name__ == "__main__":
    main()