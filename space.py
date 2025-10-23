import pygame,time,pyautogui,random
pygame.init()
W,H=pyautogui.size()
canvas=pygame.display.set_mode((W,H))
pygame.display.set_caption("space invader")
bg=pygame.transform.scale(pygame.image.load("space.png"),(W,H))
sw,sh=70,70
redship=pygame.transform.scale(pygame.image.load("spaceship.png"),(sw,sh))
yellowship=pygame.transform.scale(pygame.image.load("spaceship2.png"),(sw,sh))
redship=pygame.transform.rotate(redship,-90)
yellowship=pygame.transform.rotate(yellowship,90)
border=pygame.Rect(W/2-10,0,20,H)
redhit=pygame.USEREVENT+1
yellowhit=pygame.USEREVENT+2
font1=pygame.font.SysFont("Times New Roman",30)
font2=pygame.font.SysFont("Arial",70)
def display(red,yellow,rbullet,ybullet,rhealth,yhealth,winner):
    canvas.blit(bg,(0,0))
    #pygame.draw.rect(canvas,"red",red)
    #pygame.draw.rect(canvas,"yellow",yellow)
    for i in rbullet:
        pygame.draw.rect(canvas,"red",i)
    for i in ybullet:
        pygame.draw.rect(canvas, "yellow", i)
    canvas.blit(redship,(red.x,red.y))
    canvas.blit(yellowship,(yellow.x,yellow.y))
    ytext=font1.render("yhealth:-->"+str(yhealth),True,"white")
    rtext=font1.render("rhealth:-->"+str(rhealth),True,"white")
    canvas.blit(ytext,(40,40))
    canvas.blit(rtext,(W-200,40))
    if winner:
        winnertxt=font2.render("winner",True,"yellow")
        canvas.blit(winnertxt,(W/2-100,H/2))
        



    pygame.draw.rect(canvas,"black",border)
   
def handleplayers(keypressed,red,yellow):
    if keypressed[pygame.K_RIGHT] and red.x+red.width<W:
        red.x+=10
    if keypressed[pygame.K_LEFT] and red.x>border.x+border.width:
        red.x-=10
    if keypressed[pygame.K_UP] and red.y>0:
        red.y-=10    
    if keypressed[pygame.K_DOWN] and red.y+red.height<H:
        red.y+=10
    if keypressed[pygame.K_d] and yellow.x + yellow.width < border.x:
        yellow.x+=10
    if keypressed[pygame.K_a] and yellow.x>0:
        yellow.x-=10
    if keypressed[pygame.K_w] and yellow.y>0:
        yellow.y-=10
    if keypressed[pygame.K_s] and yellow.y+yellow.height<H:
        yellow.y+=10
    #yellow.x=random.randint(0,border.x-yellow.width)
    #yellow.y=random.randint(0,H-yellow.height)
    if random.randint(1,100)<5:
        x=random.randint(-100,100)
        y=random.randint(-100,100)
        #if yellow.x>100 and yellow.x<border.x-yellow.width-100 and yellow.y>100 and yellow.y<5-yellow.height-100:
        if x<0 and yellow.x>=x*(-1):
            yellow.x+=x
        if x>0 and yellow.x<=border.x-yellow.width-x:
            yellow.x+=x
        if y<0 and yellow.y>=y*(-1):
            yellow.y+=y
        if y>0 and yellow.y<=H-yellow.height-y:
            yellow.y+=y
            #yellow.y=random.randint(-100,100)
def handle_bullets(red,yellow,rbullet,ybullet):
    #print(len(ybullet))
    for i in rbullet:
        i.x-=10
        if i.x<0:
            rbullet.remove(i)
        for r in ybullet:
            if i.colliderect(r):
                ybullet.remove(r)
                rbullet.remove(i)
                break
        if i.colliderect(yellow):
            print("yellow got hit")
            pygame.event.post(pygame.event.Event(yellowhit))
            
            rbullet.remove(i)
            
    for i in ybullet:
        if i.colliderect(red):
            ybullet.remove(i)
            print("red got hit")
            pygame.event.post(pygame.event.Event(redhit))

        i.x+=10
        if i.x>W:
            ybullet.remove(i)

    
def main():
    red=pygame.Rect(W-100,H/2,70,70)
    yellow=pygame.Rect(100,H/2,sw,sh)
    rbullet=[]
    ybullet=[]
    rhealth=10
    yhealth=10
    winner=None
    while 1:
        display(red,yellow,rbullet,ybullet,rhealth,yhealth,winner)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE:
                    b=pygame.Rect(red.x,red.y+red.height/2,20,8)
                    rbullet.append(b)
            if i.type==redhit:
                rhealth-=1
            if i.type==yellowhit:
                yhealth-=1
        if rhealth==0:
            winner="yellow wins"
        if yhealth==0:
            winner="red wins"
        



        if random.randint(1, 100) < 3:
            g=pygame.Rect(yellow.x, yellow.y + yellow.height / 2, 20, 8)
            ybullet.append(g)
        keypressed=pygame.key.get_pressed()
        handleplayers(keypressed,red,yellow)
        handle_bullets(red,yellow,rbullet,ybullet)

        pygame.display.update()

main()