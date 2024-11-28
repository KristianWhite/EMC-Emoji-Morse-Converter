import pygame
import pygame.freetype



def main():
    pygame.init()
    pygame.font.init()
    
    # Display Screen
    pygame.display.set_caption("EMC")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    # Load new icon image
    new_icon = pygame.image.load(r"C:\Users\Krist\Documents\Python\ANGM2305\EMC-Emoji-Morse-Converter\src\smilley.ico")
    pygame.display.set_icon(new_icon)
    
    # Run mode_switch
    mode_switch(screen)
    
    # Main event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()




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
    
    message = ""
    Mode = ""

    # Initialize the font here
    Input_font = pygame.font.Font(None, 32)  # Use a default font for now
    Output_font = pygame.freetype.SysFont("segoeuisymbol", 50)

    def draw_text(text, Input_font, text_col, x, y):
        img = Input_font.render(text, True, text_col)
        screen.blit(img, (x, y))
    
    input_active = True
    
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    Mode = Mode[:-1]
                else:
                    Mode += event.unicode
        
        # Render the text
        screen.fill("red")
        draw_text("Type encrypt to Convert:", Input_font, (255, 255, 255), 260, 100)
        pygame.draw.rect(screen, "gray", (150,150,500,30), width = 5, border_radius = 10)
        pygame.draw.circle(screen, "gray", (400,350), 60, 0, False, False, False, False)
        pygame.draw.circle(screen, "black", (400,350), 30, 0, False, False, False, False)
        draw_text(Mode, Input_font, (255, 255, 255), 260, 155)
        pygame.display.flip()
    
    #Transition to type message
    if Mode.lower() == "encrypt":
        Encrypt_mode = True
    
    input_active = True
    message = ""
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    message = message[:-1]
                else:
                    message += event.unicode
        
        # Render the text
        screen.fill((0, 0, 0))
        draw_text("Type your message:", Input_font, (255, 255, 255), 260, 100)
        draw_text(message, Input_font, (255, 255, 255), 260, 150)
        
        pygame.display.flip()
    
    # Display the edited message
    if Encrypt_mode:
        Size = ""
        screen.fill((0, 0, 0))
        encrypted_message = letter_to_emoji(message.upper())
        pygame.draw.rect(screen, "gray", (30,200,750,190), width = 95, border_radius = 100)
        draw_text("Encrypted Message:", Input_font, "white", 100, 100)
        emoji_text, rect = Output_font.render(encrypted_message, "white",None)
        rect.center = screen.get_rect().center
        
        screen.blit(emoji_text, rect)
        print(emoji_text)
        
    pygame.display.flip()


#Display Textbox
def text_box(screen):
    input_box = pygame.Rect(100, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting...")
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