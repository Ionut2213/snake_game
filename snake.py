import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


dis_width = 400
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Joc cu Sarpe')


clock = pygame.time.Clock()

snake_block = 10
snake_speed = 20


font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 50)

def show_score(score):
    value = score_font.render(f"Score: {score}", True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    lenght_of_snake = 1

    score = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) /10.0) * 10.0


    while not game_over:
        while game_close ==True:
            dis.fill(blue)
            message("Jocul a luat sfarsit ! Apasa Q-Exit sau C pentru a juca o noua runda")
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = - snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = - snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for x in snake_list[: -1]:
            if x == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(dis, black, [segment[0], segment[1], snake_block, snake_block])

        show_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            lenght_of_snake += 1
            score += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()




