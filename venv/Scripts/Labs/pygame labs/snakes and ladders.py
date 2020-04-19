import pygame
import os
import random
import time

pygame.init()
pygame.font.init()

width, hight = 755, 850
win = pygame.display.set_mode((width,hight))
pygame.display.set_caption("Snakes & Ladders")
dise = list(range(1,7))

RED = pygame.image.load(os.path.join("img", "red.png"))
YEL = pygame.image.load(os.path.join("img", "yellow.png"))

BG = pygame.image.load(os.path.join("img", "snakesladdersprintable.jpg"))

class button():
    def __init__(self, color, x, y, b_width, b_hight, lable=""):
        self.color = color
        self.x = x
        self. y = y
        self. b_width = b_width
        self. b_hight = b_hight
        self.lable = lable

    def draw_button(self, win, outline=None):
        """Method to draw button on screen"""
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.b_width + 4, self.b_hight + 4 ), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.b_width, self.b_hight), 0)

        if self.lable != "":
            button_font = pygame.font.SysFont('comicsans', 50)
            text = button_font.render(self.lable, 1, (0,0,0))
            win.blit(text, (self.x + (self.b_width/2 - text.get_width()/2),
                            self.y + (self.b_hight/2 - text.get_height()/2)))

    def isOverButton(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.b_width:
            if pos[1] > self.y  and pos[1] < self.y + self.b_hight:
                return True
        return False

class pices():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None

    def draw_shape(self, win):
        win.blit(self.img, (self.x, self.y))

class player(pices):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = RED



main_font = pygame.font.SysFont("comicsans", 50)

test_button = button((0,255,0), 10, 780, 160, 40, "Roll Dise")

red = player(10,700)

def display_info(turn, roll):

    display_roll = main_font.render(f"Dise roll: {roll}", 1, (255, 0, 255))
    display_turn = main_font.render(f"{turn} Turn", 1, (255, 0, 0))

    win.blit(display_roll, (width - display_roll.get_width() - 10, hight - display_roll.get_height() - 10))
    win.blit(display_turn, (width - display_turn.get_width() - 10, hight - display_turn.get_height() - 50))

def dise_roll():
    roll = random.choice(dise)
    return roll

def redrawWindow(turn, roll):
    win.fill(pygame.Color("black")) # To Clear screen
    win.blit(BG, (0, 0)) #To set background
    test_button.draw_button(win, (255,0,0))
    red.draw_shape(win)
    display_info(turn, roll)
    pygame.display.update()

def check_square(x, y):
   snakes = [ ]
   ladder_x = [ 160, 385, 685, 385, 160, 535 ]
   ladder_y = [ 700, 700, 624, 472, 244, 244 ]

   if x > 690:
       x = 10
       y = y - 76
       if y < 10:
           y = 700
   if x in ladder_x and y in ladder_y:
       if x == 160 and y == 700: #3
            x = 10
            y = 320
       elif x == 385 and y == 700: #6
            x = 460
            y = 548
       elif x == 685 and y == 624: #20
            x = 685
            y = 244
       elif x == 385 and y == 472: #36
            x = 310
            y = 320
       elif x == 160 and y == 244: #63
            x = 310
            y = 16
       elif x == 535 and y == 244: #68
            x = 535
            y = 16

   return x, y



def main():
    FPS = 60
    #clock = pygame.time.Clock()
    roll = 0
    turn = "Player"
    right = 10
    up = 700

    run = True
    while run:
        #clock.tick(FPS)
        redrawWindow(turn, roll)



        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if test_button.isOverButton(pos):
                    test_button.color = (255,0,0)
                    roll = dise_roll()

                    if turn == "Player":
                        right = right + (75 * roll)
                        print(right)
                        right, up = check_square(right, up)
                        red.x = right
                        red.y = up

            if event.type == pygame.MOUSEBUTTONUP:
                if test_button.isOverButton(pos):
                    test_button.color = (0,255,0)








if __name__ == "__main__":
    main()



