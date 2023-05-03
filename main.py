import random
import time

import pygame

import sys

from config import commandsCountMassive, field, commandsCountMassiveCoordinates, commandsCount, blockCount
from handler import _handler

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 255)

pygame.init()
infoObject = pygame.display.Info()

print(infoObject)

WINDOW_WIDTH = infoObject.current_w // 100 * 55
WINDOW_HEIGHT = WINDOW_WIDTH


if blockCount > WINDOW_WIDTH:
    print(f'Для твоего экрана максимальное кол-во клеток - {WINDOW_WIDTH}')
    sys.exit()
blockSize = int(WINDOW_WIDTH / blockCount)
if blockSize == 0:
    blockSize = 1
print(f'{blockCount} - {blockSize} - {WINDOW_WIDTH}')

for x in range(commandsCount):
    commandsCountMassive.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])


def main():
    global SCREEN, CLOCK

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        time_start = time.time()
        mouse = pygame.mouse.get_pos()
        drawGrid(mouse)
        _handler()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        print(f'Время на обработку: {time.time() - time_start}')
        # time.sleep(0.05)


def drawGrid(mouse):
    global field
    time_start = time.time()
    x_field, y_field = 0, 0
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            if y + blockSize <= WINDOW_HEIGHT and x + blockSize <= WINDOW_WIDTH and y_field < blockCount and x_field < blockCount:
                # print(f'{x_field} {y_field}')
                rect = pygame.Rect(x, y, blockSize, blockSize)
                if x < mouse[0] < x + blockSize and y < mouse[1] < y + blockSize:
                    pygame.draw.rect(SCREEN, WHITE, rect, 1)
                else:
                    pygame.draw.rect(SCREEN,
                                     (field[x_field][y_field][0],
                                      field[x_field][y_field][1],
                                      field[x_field][y_field][2]),
                                     rect)
                y_field += 1
        x_field += 1
        y_field = 0

    # print(f'Рисовка поля длилась - {time.time() - time_start}')


for x in range(blockCount):
    y_line = []
    for y in range(blockCount):
        y_line.append([0, 0, 0, 0])
    field.append(y_line)
ind_x = 0
while len(commandsCountMassiveCoordinates) != commandsCount:

    x_com, y_com = random.randint(0, len(field) - 1), random.randint(0, len(field) - 1)

    if field[x_com][y_com] == [0, 0, 0, 0]:

        field[x_com][y_com] = [commandsCountMassive[ind_x][0], commandsCountMassive[ind_x][1], commandsCountMassive[ind_x][2], 1]
        commandsCountMassiveCoordinates.append([[x_com, y_com]])
        ind_x += 1



print(commandsCountMassiveCoordinates)
print(field)

main()
