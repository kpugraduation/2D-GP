import random
import json
import os

from pico2d import *

import game_framework
import title_state
from BackGround import Background
from Player import Player_Character
from Player import Missile
from Enemy  import Monster
from Item import Item_bomb
from Item import Item_slow
import Ranking_state
name = "MainState"

boy = None
grass = None
font = None
background=None
monster=None
missiles=[]



def enter():
    global player,background,monster,item_bomb,item_slow,missile,font
    font=load_font('ENCR10B.TTF')
    player=Player_Character()
    background=Background()
    monster=Monster()
    item_bomb=Item_bomb()
    item_slow=Item_slow()
    game_framework.reset_time()


    pass


def exit():

    global player,background,monster,item_bomb,item_slow,missile,font
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()
    score_data.append({"Time": player.life_time})
    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()
    del(font)
    del(player)
    del(background)
    del(monster)
    del(item_bomb)
    del(item_slow)
    #del(missile)

    pass


def pause():
    pass


def resume():
    pass


def collide(a,b):

    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()

    if left_a>right_b : return False
    if right_a<left_b : return False
    if top_a<bottom_b : return False
    if bottom_a>top_b : return False

    return True

def handle_events(frame_time):

    global missiles
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.change_state(Ranking_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            newmisslies = Missile(player.x,player.y)
            missiles.append(newmisslies)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            item_bomb.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            item_slow.handle_event(event)
        else:
            player.handle_event(event)



    pass



def update(frame_time):

    global monsters
    handle_events(frame_time)

    monster.update(frame_time)

    for missile in missiles:
        missile.update()

    for missile in missiles:
        if collide(monster, missile):
            missile.remove(missile)
            monsters.remove(monster)

    '''
    for monster in monsters:
        if collide(monster, player):
             close_game = 1
            game_framework.push_state(Ranking_state)
    '''
    #monster.update(frame_time)
    player.update(frame_time)
    background.update()
    font.draw(500,450,'Time:%4.1f'%(player.life_time),(0,0,0))
    print(player.life_time)
    #font.draw(100, 450 - 40 * i, 'TIME:%4.1f'
           #   % (score['Time']), (100, 150, 150))


def draw(frame_time):
    clear_canvas()
    background.draw()
    player.draw()
    monster.draw()
    item_bomb.draw()
    item_slow.draw()
    for missile in missiles:
        missile.draw()
    update_canvas()



    delay(0.02)
    pass





