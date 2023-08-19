import pygame, sys
from pytmx.util_pygame import load_pygame



class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame('../data/tmx/basic.tmx')
sprite_group = pygame.sprite.Group()

for layer in tmx_data.visible_layers:
    #if layer.name in ('Floor', 'Plants and rocks', 'Pipes'):
    if hasattr(layer, 'data'):
        for x,y,surf in layer.tiles():
            pos = (x * 128, y * 128)
            Tile(pos = pos, surf= surf,groups= sprite_group)

for obj in tmx_data.objects:
    pos = obj.x, obj.y
    if obj.image:
        Tile(pos = pos,surf= obj.image, groups = sprite_group)


# print(tmx_data.layers)
# for layer in tmx_data.visible_layers:
#     print(layer)
#
# print(tmx_data.layernames)
#
# print(tmx_data.get_layer_by_name('Floor'))
#
# for obj in tmx_data.objectgroups:
#     print(obj)

# layer = tmx_data.get_layer_by_name('Floor')
# for x, y, surf in layer.tiles():
#     print(x * 128)
#     print(y * 128)
#     print(surf)

# print(layer.data)

# print(layer.name)
# print(layer.id)


#object_layer = tmx_data.get_layer_by_name('Objects')
#for obj in object_layer:
    # print(obj.x)
    # print(obj.y)
    # print(obj.image)
    # if obj.type == 'Shape':
    #     if obj.name =='Marker':
    #         print(obj.x)
    #         print(obj.y)

# for obj in tmx_data.objects:
#     print(obj)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)
    for obj in tmx_data.objects:
        pos = obj.x, obj.y
        if obj.name in ('Rectangle', 'Polygon', 'Elipse', 'Marker'):
            if obj.name == 'Marker':
                pygame.draw.circle(screen,'red',pos,5)
            if obj.name == 'Rectangle':
                rect = pygame.Rect(obj.x , obj.y , obj.width ,obj.height)
                pygame.draw.rect(screen,'yellow',rect)
            if obj.name == 'Elipse':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                pygame.draw.ellipse(screen,'blue',rect)


    pygame.display.update()