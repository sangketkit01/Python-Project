import pygame as py
clock = py.time.Clock()

start = py.time.get_ticks()
while True :
    x = py.time.get_ticks()
    print(x-start)