import pygame
import time
import sys

pygame.init()
pygame.joystick.init()

# Check for connected controllers
if pygame.joystick.get_count() == 0:
    print("No controller detected. Connect your controller and try again.")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected: {joystick.get_name()}")

# Choose buttons to monitor; uncomment the print line below to identify them.
BUTTON_TO_HOLD = 1 
BUTTON_TO_DISABLE_MONITORING = 2
"""
8bitdo SN30 mapping:
B: 0
A: 1
Y: 2
X: 3
SELECT: 4
LT: 9
RT: 10
LEFT: 13
RIGHT: 14
UP: 11
DOWN: 12
"""

held = False

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                # Uncomment to find the right button ID
                print(f"got button: {event.button}")
                if event.button == BUTTON_TO_HOLD:
                    held = True
                    print("Button held. Monitoring hold.")
                    joystick.rumble(0, 0, 0)
            
                if event.button == BUTTON_TO_DISABLE_MONITORING:
                    held = False
                    print("Hold monitoring disabled.")
                    joystick.stop_rumble()


            elif event.type == pygame.JOYBUTTONUP:
                if event.button == BUTTON_TO_HOLD:
                    held = False
                    print("Button released. Vibrating...")
                    joystick.rumble(0, 0.02, 0)  # low_freq, high_freq, duration (0 = indefinite)
            
        time.sleep(0.01)  # Small delay to not hog CPU

except KeyboardInterrupt:
    print("Exiting...")
    joystick.stop_rumble()
    pygame.quit()