import time
import pygame
import sys
import random

pygame.init()
CLOCK = pygame.time.Clock()


width = 300
hight = 400
red = (255, 50, 50)
white = (255, 255, 255)
black = (0, 0, 0)
board = [[None] * 3, [None] * 3, [None] * 3]
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("ahmed's tick tack toe")
font = pygame.font.SysFont('timesnewroman', 40)
text_x = font.render('X', True, red)
text_o = font.render('O', True, red)

def human_player():
    user_click()

def random_computer_player(): # gives random x & , turned to row & col
    global  board
    while True:
        x = random.randint(0,300)
        y = random.randint(0,300)

        if (x < 100):
            col = 1
        elif (x < 200):
            col = 2
        elif x < 300:
            col = 3

        if y < 100:
            row = 1
        elif y < 200:
            row = 2
        elif y < 300:
            row = 3

        if row and col and board[row - 1][col - 1] is None:
            type_xo(row, col)
            check_win()
            break


def draw_status(): # write message only
    global draw, white
    message = ' '
    font = pygame.font.SysFont("timesnewroman", 40)

    pygame.event.get()
    if winner is not None:
        message = winner.upper() + " won !"

    if draw:
        message = "Game Draw !"

    text = font.render(message, 1, white)
    screen.blit(text, (50, 320))
    pygame.display.update()

#def available_moves():
    #return [i for i,x in enumerate(board) if x == None]

def check_win():
    global board, winner, draw
    for row in range(3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row] is not None)):
            winner = board[row][0]
            break
    for col in range(3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[col] is not None)):
            winner = board[0][col]
            break

        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            winner = board[0][0]
            break
    if (winner is None):
        if (board[0][2] == board[1][1] == board[2][0]) and (board[2][0] is not None):
            winner = board[0][2]

        elif (board[2][2] == board[1][1] == board[0][0]) and (board[1][1] is not None):
            winner = board[1][1]

        elif (all([all(row) for row in board])):
            draw = True

    draw_status()

def type_xo(row, col):
    global board, xo

    if row == 1:
        posx = 30
    if row == 2:
        posx = 130
    if row == 3:
        posx = 230
    if col == 1:
        posy = 30
    if col == 2:
        posy = 130
    if col == 3:
        posy = 230

    board[row - 1][col - 1] = xo
    if (xo == 'x'):
        pygame.draw.rect(screen, black, [0, 305, 300, 100])
        screen.blit(text_x, (posy, posx))
        xo = 'o'

    else:
        pygame.draw.rect(screen, black, [0, 305, 300, 100])
        screen.blit(text_o, (posy, posx))
        xo = 'x'
    pygame.display.update()

def user_click(): # takes a mouse position ,
    pygame.event.get()
    x, y = pygame.mouse.get_pos()
    if (x < 100):
        col = 1
    elif (x < 200):
        col = 2
    elif x < 300:
        col = 3
    else:
        col = None

    if y < 100:
        row = 1
    elif y < 200:
        row = 2
    elif y < 300:
        row = 3
    else:
        row = None

    if row and col and board[row - 1][col - 1] is None:
        type_xo(row, col)
        check_win()

def reset_game(): # set board, draw lines, goes to draw, starting with x
    global board, winner, xo, draw, message

    xo = 'x'
    draw = False
    message = ' '
    winner = None
    board = [[None] * 3, [None] * 3, [None] * 3]
    screen.fill(black)
    pygame.draw.line(screen, red, [100, 0], [100, 300], 5)
    pygame.draw.line(screen, red, [200, 0], [200, 300], 5)
    pygame.draw.line(screen, red, [0, 100], [300, 100], 5)
    pygame.draw.line(screen, red, [0, 200], [300, 200], 5)
    pygame.draw.line(screen, red, [0, 300], [300, 300], 5)
    draw_status()

def play():
    reset_game()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                user_click()
                if winner is None and draw is False:
                    time.sleep(1)
                    random_computer_player()
                if winner or draw:
                    time.sleep(2)
                    reset_game()


        pygame.display.update()

play()
