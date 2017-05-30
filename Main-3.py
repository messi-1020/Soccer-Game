from pygame.locals import *
import pygame, sys
from math import pi


FPS = 200

WindowWidth   = 850
WindowHeight  = 450
lineThickness = 5
playerSize = 10
paddleOffSet = 5


#Colors
Green = ( 50,205, 50)
White = (255,255,255)
Red   = (255,  0,  0)
Blue  = (  0,  0,255)
Shade_of_Green = (  0,128,  0)
Black = (  0,  0,  0)
yellow = (255,255,  0)


def WelcomeSceen():

    DrawField()

    End_Menue = False
    while End_Menue == False:


        myFont= pygame.font.SysFont("Arial",80,1,1)
        font = pygame.font.SysFont("Arial",38,1,2)
        Welcome = myFont.render("Welcome",0,Red)
        Press = font.render("Press to Play", 0,Red)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN :
                End_Menue = True

            else:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        DisplaySurf.blit(Welcome,[WindowWidth/2 - 175, WindowHeight/2 - 100])
        DisplaySurf.blit(Press, [WindowWidth /2 - 125, WindowHeight/2 ])
        pygame.display.flip()



def DrawField():


    DisplaySurf.fill(Green) #Fills the color for the field
    pygame.draw.rect(DisplaySurf, White, ((50,50), (750, 350)), lineThickness ) # Boundaries for the field
    pygame.draw.rect(DisplaySurf,Shade_of_Green, [0,0,850,450],75)

    #Mid-Field
    pygame.draw.line(DisplaySurf, White, (WindowWidth / 2, 50),(WindowWidth/2, 400), 5 ) # Mid-line
    pygame.draw.circle(DisplaySurf, White, [425, 225], 8) # Ball Starting Position location
    pygame.draw.ellipse(DisplaySurf, White,[350,150,150,150],lineThickness)

    #Goal boxes
        #Left
    pygame.draw.rect(DisplaySurf, White, [50,125, 100, 200],lineThickness) #Big Rec
    pygame.draw.rect(DisplaySurf, White, [50,175, 40, 100], lineThickness) #Small Rec
    pygame.draw.line(DisplaySurf, Red,(50, 180), (50, 270), lineThickness)
    pygame.draw.arc(DisplaySurf, White, [100,180,100,100], 0,pi/2, lineThickness)
    pygame.draw.arc(DisplaySurf, White, [100,180,100,100], 3* pi/2, 2 * pi, lineThickness)
    pygame.draw.circle(DisplaySurf, White, [120, 225], 5)

        #Right
    pygame.draw.rect(DisplaySurf, White, [WindowWidth - 50, 125, -100,200], lineThickness)# Big right rectangle
    pygame.draw.rect(DisplaySurf, White, [WindowWidth -50, 175, -40, 100], lineThickness) # Small right rectangle
    pygame.draw.line(DisplaySurf, Blue, (WindowWidth -50, 180),(WindowWidth- 50, 270), lineThickness) # Right Blue Goal Line
    pygame.draw.arc(DisplaySurf,White, [WindowWidth-200, 180,100,100], pi/2, pi, lineThickness)
    pygame.draw.arc(DisplaySurf, White, [WindowWidth-200, 180,100,100], pi, 3*pi/2,lineThickness)
    pygame.draw.circle(DisplaySurf, White, [WindowWidth -120, 225], 5)

#Draws the Ball
def DrawBall(ball):

    pygame.draw.circle(DisplaySurf, Black ,ball, lineThickness)

def LeftPlayers(RedPlayer1, RedPlayer2):

     pygame.draw.rect(DisplaySurf, Red, RedPlayer1)
     pygame.draw.rect(DisplaySurf, Red, RedPlayer2)

#Main function
def main():

    pygame.init()

    global DisplaySurf
    FPSCLOCK = pygame.time.Clock()
    DisplaySurf = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Pro Soccer")

    #Inititate variable and set starting positions
    ballX = 425
    ballY = 225

    #Red forward players starting position
    RedPlayerX = 375
    RedPlayerY = 110




    ball = [ballX, ballY] # In the center of the field
    #Red team forward players
    RedPlayer1 = pygame.Rect(RedPlayerX, RedPlayerY, playerSize, lineThickness + 5)
    RedPlayer2 = pygame.Rect(RedPlayerX, RedPlayerY + 50, playerSize, lineThickness + 5)






    WelcomeSceen()
    DrawField()


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DrawBall(ball)
        LeftPlayers(RedPlayer1, RedPlayer2)


        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
