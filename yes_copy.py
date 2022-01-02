import wiringpi as w
import os
import pygame

w.wiringPiSetup()
w.pwmSetMode(1)
w.pwmSetClock(2)
w.pwmSetRange(480)
pygame.init()
done = False
clock = pygame.time.Clock()

pygame.joystick.init()

# -------- Main Program Loop -----------
while done == False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

 
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        button = joystick.get_button(1)#a:0: b:1 x:3 y:4 lb:6 rb:7 lt:8 rt:9
        print(button)
        if button == 0:
            w.pinMode(1,1)
            w.pinMode(26,1)
            w.digitalWrite(1,1)
            w.digitalWrite(26,1)
        else:
            w.pinMode(1, 2)
            w.pinMode(26, 2)
            w.pwmWrite(1,50)
            w.pwmWrite(26, 50)
pygame.quit()          