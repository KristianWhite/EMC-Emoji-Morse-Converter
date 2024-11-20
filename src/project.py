import pygame
import sys
import pygame_gui

#Display the Text corresponding with the input and the result when choosing modes
def main():
    
    pygame.init()
    pygame.display.set_caption("EMC")
    resolution = (800, 600)
    dt = 0
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    mode_switch(screen)



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

def mode_switch(screen):
    Encrypt_mode = False
    Deciph_mode = False
    
    message = ""
    Mode = ""
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    
    input_active = True
    pygame.display.set_caption("EMC")
    
    # Set up the font
    font = pygame.font.Font(None, 32)
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    Mode = Mode[:-1]
                else:
                    Mode += event.unicode
        
        # Render the text
        screen.fill((0, 0, 0))
        draw_text("Choose mode: Encrypt or Deciph:", font, (255, 255, 255), 100, 100)
        draw_text(Mode, font, (255, 255, 255), 100, 150)
        pygame.display.flip()
    
    if Mode.lower() == "encrypt":
        Encrypt_mode = True
    elif Mode.lower() == "deciph":
        Deciph_mode = True
    
    input_active = True
    message = ""
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    message = message[:-1]
                else:
                    message += event.unicode
        
        # Render the text
        screen.fill((0, 0, 0))
        draw_text("Type your message:", font, (255, 255, 255), 100, 100)
        draw_text(message, font, (255, 255, 255), 100, 150)
        pygame.display.flip()
    
    if Encrypt_mode:
        encrypted_message = letter_to_emoji(message.upper())
        draw_text("Encrypted Message:", font, (255, 255, 255), 100, 200)
        draw_text(encrypted_message, font, (255, 255, 255), 100, 250)
    elif Deciph_mode:
        decrypted_message = emoji_to_letter(message.upper())
        draw_text("Decrypted Message:", font, (255, 255, 255), 100, 200)
        draw_text(decrypted_message, font, (255, 255, 255), 100, 250)

    
    pygame.display.flip()

def text_box(screen):
    input_box = pygame.Rect(100, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0, 0, 0))
        txt_surface = text.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()



if __name__ == "__main__":
        main()