import pygame

MAX_X = 1920
MAX_Y = 1080
game_over = False
bg_color = (0 , 0 , 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("Free Kherson")

myimage = pygame.image.load("1.png") .convert()
myimage = pygame.transform.scale(myimage, (571, 1280))

x = 700
y = 100

move_right = False
move_left = False
move_up = False
move_down = False

while game_over == False:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left == True:
            x = x - 2
            if x < 0:
                x = 0

    if move_right == True:
            x = x + 2
            if x > MAX_X - 571:
                x = MAX_X - 571

    if move_up == True:
            y = y - 2
            if y < 0:
                y = 0

    if move_down == True:
            y = y + 2
            if y > MAX_Y - 1280:
                y = MAX_Y - 1000


    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()






