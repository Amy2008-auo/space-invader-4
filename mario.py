import pyautogui,time,pygame,random
pygame.init()
W,H=pyautogui.size()
canvas=pygame.display.set_mode((W,H))
pygame.display.set_caption("Mario vs Bowser")
bg=pygame.transform.scale(pygame.image.load("mariobg.jpg"),(W,H))
mw,mh=200,250
bw,bh=200,300
bowser=pygame.transform.scale(pygame.image.load("bowser.png"),(bw,bh))
mario=pygame.transform.scale(pygame.image.load("mario1.png"),(mw,mh))
bowser=pygame.transform.rotate(bowser,-0)
mario=pygame.transform.rotate(mario,0)
border=pygame.Rect(W/2-10,0,20,H)

def display(blue,green,mbullet,bbullet):
    canvas.blit(bg,(0,0))
    for i in mbullet:
        pygame.draw.rect(canvas,"blue",i)
    for i in bbullet:
        pygame.draw.rect(canvas, "green", i)
    canvas.blit(bowser,(green.x, green.y))
    canvas.blit(mario,(blue.x, blue.y))

    pygame.draw.rect(canvas,"black",border)

def handleplayers(keypressed,blue,green):
    if keypressed[pygame.K_RIGHT] and green.x+green.width<W:
        green.x+=10
    if keypressed[pygame.K_LEFT] and green.x>border.x+border.width:
        green.x-=10
    if keypressed[pygame.K_UP] and green.y>0:
        green.y-=10    
    if keypressed[pygame.K_DOWN] and green.y+green.height<H:
        green.y+=10
    if keypressed[pygame.K_d] and blue.x + blue.width < border.x:
        blue.x+=10
    if keypressed[pygame.K_a] and blue.x>0:
        blue.x-=10
    if keypressed[pygame.K_w] and blue.y>0:
        blue.y-=10
    if keypressed[pygame.K_s] and blue.y+blue.height<H:
        blue.y+=10
    
    if random.randint(1,100)<5:
        x=random.randint(-100,100)
        y=random.randint(-100,100)
        if x<0 and green.x>=x*(-1):
            green.x+=x
        if x>0 and green.x<=border.x-green.width-x:
            green.x+=x
        if y<0 and green.y>=y*(-1):
            green.y+=y
        if y>0 and green.y<=H-green.height-y:
            green.y+=y

def handle_bullets(blue,green,mbullet,bbullet):
    #print(len(ybullet))
    for i in mbullet:
        i.x+=10
        if i.x<0:
            mbullet.remove(i)
        for r in bbullet:
            if i.colliderect(r):
                bbullet.remove(r)
                mbullet.remove(i)
                break
        if i.colliderect(green):
            print("green got hit")
            mbullet.remove(i)
            
    for i in bbullet:
        if i.colliderect(blue):
            bbullet.remove(i)
            print("blue got hit")

        i.x-=10
        if i.x>W:
            bbullet.remove(i)

def main():
    green=pygame.Rect(W-200,H/2,mw,mh)
    blue=pygame.Rect(100,H/2,bw,bh)
    mbullet,bbullet=[],[]
    while 1:
        display(blue,green,mbullet,bbullet)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LCTRL:
                    b=pygame.Rect(blue.x,blue.y+blue.height/2,20,8)
                    mbullet.append(b)
        if random.randint(1, 100) < 3:
            g=pygame.Rect(green.x, green.y + green.height / 2, 20, 8)
            bbullet.append(g)
        keypressed=pygame.key.get_pressed()
        handleplayers(keypressed,blue,green)
        handle_bullets(blue,green,mbullet,bbullet)

        pygame.display.update()
main()