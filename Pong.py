# Pong Game

import pygame
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,211,67)
GREEN = (0,255,0)

pygame.init()

# Create the display window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong: Use the left and right arrow keys to move the paddle, or press 'ESC' to exit the game")
time.sleep(1)

# Initial coordinates of the paddle
paddle_x = 400
paddle_y = 580

# Initial speed of the paddle
paddle_change_x = 0
paddle_change_y = 0

# Initial position of the ball
ball_x = 50
ball_y = 50

# Speed of the ball
ball_change_x = 5
ball_change_y = 5

score = 0

# Draw the paddle and restrict its movement between the edges of the window
def drawrect(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699
    pygame.draw.rect(screen,RED,[x,y,100,10])

# The game's main loop
done = False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_change_x = -6
            elif event.key == pygame.K_RIGHT:
                paddle_change_x = 6
            elif event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_change_y = 0            
    screen.fill(BLACK)
    paddle_x += paddle_change_x
    paddle_y += paddle_change_y
    
    ball_x += ball_change_x
    ball_y += ball_change_y
    
    # This handles the movement of the ball
    if ball_x<0:
        ball_x=0
        ball_change_x = ball_change_x * -1
    elif ball_x>785:
        ball_x=785
        ball_change_x = ball_change_x * -1
    elif ball_y<0:
        ball_y=0
        ball_change_y = ball_change_y * -1
    elif ball_x>paddle_x and ball_x<paddle_x+100 and ball_y==575:
        ball_change_y = ball_change_y * -1
        score = score + 1
    elif ball_y>600:
        ball_change_y = ball_change_y * -1
        score = 0                        
    pygame.draw.rect(screen,WHITE,[ball_x,ball_y,15,15])
    
    # Draw the ball (square)
    drawrect(screen,paddle_x,paddle_y)
    
    # The score board
    font= pygame.font.SysFont('Arial', 18, False, False)
    text = font.render("Score = " + str(score), True, YELLOW)
    screen.blit(text,[600,100])
       
    pygame.display.flip()
    clock.tick(60)

    if (done == True):
        pygame.display.set_caption("Pong: Your final score is " + str(score) + " point(s)")
        time.sleep(2)

pygame.quit()
