import pygame
import sys

def play():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)


import random

WIDTH = 10
HEIGHT = 10

def play():
    snake = [[5, 5]]
    food = [random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)]
    score = 0

    while True:
        print("\n" * 3)

        for y in range(HEIGHT):
            row = ""
            for x in range(WIDTH):
                if [y, x] == snake[0]:
                    row += "O "
                elif [y, x] in snake:
                    row += "o "
                elif [y, x] == food:
                    row += "* "
                else:
                    row += ". "
            print(row)

        print(f"\nScore: {score}")
        move = input("Move (w/a/s/d, q=quit): ").lower()

        if move == "q":
            break

        head = snake[0][:]

        if move == "w":
            head[0] -= 1
        elif move == "s":
            head[0] += 1
        elif move == "a":
            head[1] -= 1
        elif move == "d":
            head[1] += 1
        else:
            continue

        if (
            head[0] < 0 or head[0] >= HEIGHT or
            head[1] < 0 or head[1] >= WIDTH or
            head in snake
        ):
            print("💀 Game Over!")
            print("Final Score:", score)
            break

        snake.insert(0, head)

        if head == food:
            score += 1
            food = [random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)]
        else:
            snake.pop()



from games.snake import play as snake_game



6. Snake Game


elif choice == "6":
    if current_user:
        snake_game()
    else:
        print("আগে Login করুন!")



