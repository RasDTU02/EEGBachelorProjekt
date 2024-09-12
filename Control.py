from gtts import gTTS
import os
from io import BytesIO
import pygame
import random
from google.cloud import texttospeech

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
font = pygame.font.Font(None,74)

button_rect = pygame.Rect(540,320,200,100)

def draw_button():
    pygame.draw.rect(screen,black,button_rect)
    text_surf = font.render("Start", True, white)
    screen.blit(text_surf,(button_rect.x + 40, button_rect.y + 20))

def countdown():
    for i in range(3, 0, -1):
        screen.fill(white)
        countdown_text = font.render(str(i), True, black)
        screen.blit(countdown_text, (640, 360))
        pygame.display.flip()
        pygame.time.wait(1000)

def play_audio_period(duration):
    pygame.mixer.init()
    text = "test"
    input_text = texttospeech.SynthesisInput(text=text)
    #tts = gTTS(text=text, tld="dk", lang='da')

    client = texttospeech.TextToSpeechClient()

    voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    name="en-US-Wavenet-D", 
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    pitch=2.0,  # Adjust pitch
    speaking_rate=1.1  # Adjust speed
    )
    response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
    )

    output = response.audio_content
    audio_file = BytesIO(output)
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    pygame.mixer.music.load(audio_file, 'mp3')

    start_time = pygame.time.get_ticks()

    while (pygame.time.get_ticks() - start_time) < (duration * 1000):
        pygame.mixer.music.play()


        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        break_duration = random.uniform(0.5,2.0)
        pygame.time.wait(int(break_duration * 1000))

def show_finish():
    screen.fill(white)
    finish_text = font.render('Finish', True, black)
    screen.blit(finish_text, (540, 360))
    pygame.display.flip()
    pygame.time.wait(2000)


running = True
audio_started = False

while running:
    screen.fill(white)
    draw_button()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not audio_started:
                countdown()
                play_audio_period(duration = 15)
                show_finish()
                audio_started = True

pygame.quit()