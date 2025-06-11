import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("orange")

class circle():
    def __init__(self,r,x,y,color):
        self.surf=screen
        self.r=r
        self.x=x
        self.y=y
        self.color=color
    def draw(self):
        pygame.draw.circle(self.surf,self.color,(self.x,self.y),self.r)
    def up(self):
        self.y-=5
        pygame.draw.circle(self.surf,self.color,(self.x,self.y),self.r)

    def right(self):
        self.x+=5
        pygame.draw.circle(self.surf,self.color,(self.x,self.y),self.r)

    def big(self):
        self.r+=5
        pygame.draw.circle(self.surf,self.color,(self.x,self.y),self.r)
c1=circle(10,200,200,"red")
c1.draw()


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            c1.big()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill("orange")
                c1.up()
            if event.key==pygame.K_RIGHT:
                screen.fill("orange")
                c1.right()
    pygame.display.update()

