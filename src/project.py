import pygame
import sys
import pygame_gui

pygame.init()
pygame.display.set_caption("Rain")
WIDTH, HEIGHT = (800, 600)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50), manager=MANAGER,
                                                                        object_id="#main_text_entry"))

def main():
    
    mode_switch()
    
    
    #message = "Alcala - Harzgai Rocky Hill"
    #result = letter_to_emoji(message.upper())
    #print (result)
    #message = "😠 "
    #result = emoji_to_letter(message)
    #print (result)


morse_dict = {'A': '😠', 'B': '😁', 'C': '🥶', 'D': '🥸', 'E': '😑', 'F': '😂', 'G': '😀', 'H': '🙂‍↔️.',
    'I': '☝️', 'J': '🧑‍⚖️', 'K': '😗', 'L': '🤥', 'M': '🤑', 'N': '😐', 'O': '🧡', 'P': '😔',
    'Q': '❓', 'R': '🤖', 'S': '🙂', 'T': '👍', 'U': '🙃', 'V': '✌️', 'W': '🥴', 'X': '🩻',
    'Y': '🥱', 'Z': '🤪', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
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
    
    
    Encrypt_mode=False
    Deciph_mode=False
    
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
                sys.exit()
                
                MANAGER.process_events(event) 
        MANAGER.update(UI_REFRESH_RATE)
        
        SCREEN.fill("white")
        
        MANAGER.draw_ui(SCREEN)
        
        pygame.display.update()
    
    #Deciph_ms = emoji_to_letter(message.upper())
    #Deciph = Deciph_ms
    
    Mode = input ("Choose modes: Encrypt or Deciph:")
    if Encrypt_mode == False:
        if Mode == "Encrypt":
            Encrypt_mode=True
    while Encrypt_mode == True:
        message = input ("Type Message: ")
        encrypted_ms = letter_to_emoji(message.upper())
        return print(encrypted_ms)
    if Deciph_mode == False:
        if Mode == "Deciph":
            Deciph_mode = True
    while Deciph_mode == True:
        message = input ("Type Emoji: ")
        Deciph_ms = emoji_to_letter(message.upper())
        return print(Deciph_ms)



if __name__ == "__main__":
    main()