
import random

from pico2d import *
from Enemy import Monster



class Item_bomb:
    #monster=Monster()
    def __init__(self):
        self.x,self.y=50,100
        self.nx,self.ny=50,150
        self.bx,self.by=400,300
        self.frame=3
        self.frame2=0
        self.swit=True
        self.image=load_image('./Resource/object/item_bomb.png')
        self.Num=load_image('./Resource/ui/Number01.png')
        self.Bomb=load_image('./Resource/effect/deco_02.png')
    def draw(self):
        self.image.draw(self.x,self.y)
        self.Num.clip_draw((self.frame-1)*35,0,40,20,self.nx,self.ny)
        if(self.swit==False and self.frame>0):
            self.update()
            self.swit=True

    def update(self):
        self.Bomb.draw(self.bx,self.by)
        delay(0.05)
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_z:
            self.frame -=1
            self.swit=False




class Item_slow:
    def __init__(self):
        self.x, self.y = 750, 100
        self.nx, self.ny = 750, 150
        self.bx, self.by = 400, 300
        self.frame=3
        self.swit=True
        self.image = load_image('./Resource/object/item_break.png')
        self.Num = load_image('./Resource/ui/Number01.png')
        self.slow=load_image('./Resource/effect/slow.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        self.Num.clip_draw((self.frame-1) * 35, 0, 40, 20, self.nx, self.ny)
        if (self.swit == False and self.frame> 0):
            self.update()
            self.swit = True

    def update(self):
        self.slow.draw(self.bx,self.by)
        delay(0.05)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_x:
            self.frame -= 1
            self.swit = False