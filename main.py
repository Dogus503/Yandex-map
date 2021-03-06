import pygame
import requests
import os

l, r, delta = input().split()
api_server = "http://static-maps.yandex.ru/1.x/"
params = {"ll": ",".join([l, r]), "l": "map", "spn": ",".join([delta, delta])}
response = requests.get(api_server, params=params)
if not response:
    print("Bad coordinates")
    exit(0)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)