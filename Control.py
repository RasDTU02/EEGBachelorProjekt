from gtts import gTTS
import os
from io import BytesIO
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

button_rect = pygame.Rect(540, 320, 200, 100)

def draw_button(text):
    """Draws the start button on the screen."""
    pygame.draw.rect(screen, black, button_rect)
    text_surf = font.render(text, True, white)
    screen.blit(text_surf, (button_rect.x + 40, button_rect.y + 20))

def countdown():
    """Displays a countdown on the screen."""
    for i in range(3, 0, -1):
        screen.fill(white)
        display_round(round_num, round_texts[round_num - 1])  # Redraw the round info
        countdown_text = font.render(str(i), True, black)
        screen.blit(countdown_text, (640, 360))
        pygame.display.flip()
        pygame.time.wait(1000)

def show_close_your_eyes():
    """Displays the 'Close your eyes' message on the screen."""
    screen.fill(white)
    display_round(round_num, round_texts[round_num - 1])  # Redraw the round info
    close_eyes_text = font.render('Close your eyes', True, black)
    screen.blit(close_eyes_text, (500, 360))
    pygame.display.flip()

def play_audio_period(duration, speechtext):
    """Plays the audio for the specified duration, with random breaks."""
    pygame.mixer.init()
    
    # Create the gTTS object and generate the audio
    speech = gTTS(text=speechtext, lang='da', slow=False)
    audio_buffer = BytesIO()
    speech.write_to_fp(audio_buffer)

    # Move the buffer's position to the beginning
    audio_buffer.seek(0)

    # Load the audio into Pygame mixer from BytesIO
    pygame.mixer.music.load(audio_buffer, 'mp3')

    # Start playing the audio
    start_time = pygame.time.get_ticks()

    while (pygame.time.get_ticks() - start_time) < (duration * 1000):
        show_close_your_eyes()  # Show 'Close your eyes' message
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        break_duration = random.uniform(0.5, 2.0)
        pygame.time.wait(int(break_duration * 1000))

def show_finish():
    """Displays the finish message."""
    screen.fill(white)
    finish_text = font.render('Finish', True, black)
    screen.blit(finish_text, (540, 360))
    pygame.display.flip()
    pygame.time.wait(2000)

def display_round(round_num, round_text):
    """Displays the current round number and round description at the top of the screen."""
    screen.fill(white)  # Only clear the screen once
    round_text_surf = small_font.render(f'Round {round_num}: {round_text}', True, black)
    screen.blit(round_text_surf, (20, 20))

# Main game loop
running = True
audio_started = False
round_num = 1
round_texts = ["Unfamiliar voice", "Familiar voice"]

while running:
    # Draw the initial state of the screen
    display_round(round_num, round_texts[round_num - 1])
    draw_button("Start")
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not audio_started:
                countdown()
                play_audio_period(duration=15, speechtext="Test")
                show_finish()
                audio_started = True
                
                if round_num < 2:
                    round_num += 1
                    audio_started = False
                else:
                    running = False

pygame.quit()
