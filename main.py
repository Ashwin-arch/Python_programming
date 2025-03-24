import pygame

pygame.init()

WIDTH=900
HEIGHT=500
fps=60
black=(0,0,0)
white=(255,255,255)
gray=(255,128,128)

screen=pygame.display.set_mode([WIDTH, HEIGHT])
timer=pygame.time.clock()

running=True
while running:
    timer.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT():
            running=False
            
    pygame.display.flip()
pygame.quit()