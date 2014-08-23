import pygame, easygui,utils
pygame.init()
pygame.display.set_icon(pygame.image.load("resources/images/appicon.png"))
mixer=pygame.mixer
mixer.init()
music=mixer.music
screen=pygame.display.set_mode([1200, 750])
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
fill=screen.fill
music.set_volume(0.2)
music.load("resources/music/Theme.mp3")
titleimg=load("resources/images/title.png")
music.play(-1)
run=1
q=0
up=True
r=0
def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
def title():
    global run,q,up,r
    while run:
        if up:
            r+=2.5
            if r>=200:up=False
        
        fill([r,0,0])
        blit(titleimg, [34,10.5])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=0
                q=1
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                run=0
        flip()
    if q:pygame.quit(); raise SystemExit
r=0
up=True
def setup():
    ts=[]
    #0 = Neutral
    #1 = Red Team
    #2 = Blue Team
    #3 = Barbarians(like Neutral, but has defenses)
    rhome=utils.Territory(team=1, pos=[10, 600], adjacents=[])
    bhome=utils.Territory(team=2, pos=[740, 600], adjacents=[])
    r1=utils.Territory(team=1, pos=[60, 550], adjacents=[rhome])
    rhome.adjacents.append(r1)
    r2=utils.Territory(team=1, pos=[60, 650], adjacents=[rhome])
    rhome.adjacents.append(r2)
    r3=utils.Territory(team=1, pos=[110, 600], adjacents=[rhome,r1,r2])
    r1.adjacents.append(r3)
    r2.adjacents.append(r3)
    b1=utils.Territory(team=2, pos=[690, 550], adjacents=[bhome])
    bhome.adjacents.append(b1)
    b2=utils.Territory(team=2, pos=[690, 650], adjacents=[bhome])
    bhome.adjacents.append(b2)
    b3=utils.Territory(team=2, pos=[640, 600], adjacents=[bhome,b1,b2])
    b1.adjacents.append(b3)
    b2.adjacents.append(b3)
    gauntlet=utils.Territory(team=0, pos=[375, 600], adjacents=[b3, r3])
    b3.adjacents.append(gauntlet)
    r3.adjacents.append(gauntlet)
    upper=utils.Territory(team=3, pos=[375, 550], adjacents=[b1, r1])
    b1.adjacents.append(upper)
    r1.adjacents.append(upper)
    lower=utils.Territory(team=3, pos=[375, 650], adjacents=[b2, r2])
    b2.adjacents.append(lower)
    r2.adjacents.append(lower)
    ts=[rhome, r1, r2, r3, bhome, b1, b2, b3, gauntlet, upper, lower]
    return ts
territories=setup()
colors=[[255,255,255], [255,0,0], [0,0,255], [50,50,50]]
def redturn():
    r=1
    te=1
    while r:
        fill([0,0,0])
        for t in territories:
            t.invadable=False
            for a in t.adjacents:
                pygame.draw.line(screen, [100,100,100], t.pos, a.pos)
                if a.team==te and t.team!=te:
                    t.invadable=True
            r=10
            pygame.draw.circle(screen, colors[t.team], t.pos, r)
            if t.invadable:pygame.draw.circle(screen, colors[te], t.pos, 20, 1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                r=0
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for t in territories:
                    if distance(t.pos, pos)<10:
                        break
                else:
                    t=None
                if t!=None:
                    tnames=["Neutral", "Red", "Blue", "Barbarians"]
                    choice=easygui.choicebox(msg='%s: Owned by %s' %(t.name, tnames[t.team]), title='Dialog', choices=['Rename', 'Invade'])
                    if choice=='Rename' and (t.team==te or t.team==0 or t.team==3):
                        newname=easygui.enterbox(msg='Enter new name')
                        t.name=newname
                    elif choice=='Invade' and t.invadable:
                        if t.team==0:
                            easygui.msgbox("It's deserted, so no-one tries to stop you!")
                            t.team=te
                            return
                        else:
                            easygui.msgbox('Feature being built')
                            return
                    else:
                        easygui.msgbox("Choice invalid")
        flip()
def blueturn():
    r=1
    te=2
    while r:
        fill([0,0,0])
        for t in territories:
            t.invadable=False
            for a in t.adjacents:
                pygame.draw.line(screen, [100,100,100], t.pos, a.pos)
                if a.team==te and t.team!=te:
                    t.invadable=True
            r=10
            pygame.draw.circle(screen, colors[t.team], t.pos, r)
            if t.invadable:pygame.draw.circle(screen, colors[te], t.pos, 20, 1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                r=0
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for t in territories:
                    if distance(t.pos, pos)<10:
                        break
                else:
                    t=None
                if t!=None:
                    tnames=["Neutral", "Red", "Blue", "Barbarians"]
                    choice=easygui.choicebox(msg='%s: Owned by %s' %(t.name, tnames[t.team]), title='Dialog', choices=['Rename', 'Invade'])
                    if choice=='Rename' and (t.team==te or t.team==0 or t.team==3):
                        newname=easygui.enterbox(msg='Enter new name')
                        t.name=newname
                    elif choice=='Invade' and t.invadable:
                        if t.team==0:
                            easygui.msgbox("It's deserted, so no-one tries to stop you!")
                            t.team=te
                            return
                        else:
                            easygui.msgbox('Feature being built')
                            return
                       
                    else:
                        easygui.msgbox("Choice invalid")
        flip()
title()
music.stop()
music.load("resources/music/Map.mp3")
music.play(-1)
run=1
while run:
    easygui.msgbox("It's the Red Team's turn!")
    redturn()
    easygui.msgbox("It's the Blue Team's turn!")
    blueturn()
pygame.quit()
raise SystemExit
