import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("orange")

class rectangle():
    def __init__(self,w,h,x,y,color,t):
        self.surf=screen
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.color=color
        self.t=t

    def draw(self):
        pygame.draw.rect(self.surf,self.color,(self.x,self.y,self.w,self.h),self.t)

r1=rectangle(150,150,0,0,"blue",0)
r1.draw()
r2=rectangle(150,100,300,300,"green",0)
r2.draw()
r3=rectangle(100,100,150,100,"black",5)
r3.draw()
r4=rectangle(100,100,200,200,"red",5)
r4.draw()







run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
