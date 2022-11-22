from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.texture_importer import load_texture

app = Ursina()
grass_texture = load_texture('assets/grass3.png')
sky_night_texture = load_texture('assets/hightsky.png')
oak_texture = load_texture('assets/pelmeni.png')
tree_texture = load_texture('assets/tree.png')
sand_texture = load_texture('assets/sand.png')
dirt_texture = load_texture('assets/dirt.png')
stone_texture = load_texture('assets/stone.png')
diavolo_texture = load_texture('assets/diavolo.png')
diobrando_texture = load_texture('assets/dio-brando.png')
kira_texture = load_texture('assets/kira.png')
hand_texture = load_texture('assets/hand.png')
doski_texture = load_texture('assets/doski.png')
current_texture = grass_texture


def update():
    global current_texture

    if held_keys['1']:
        current_texture = grass_texture

    if held_keys['2']:
        current_texture = oak_texture

    if held_keys['3']:
        current_texture = tree_texture

    if held_keys['4']:
        current_texture = sand_texture

    if held_keys['5']:
        current_texture = dirt_texture

    if held_keys['6']:
        current_texture = stone_texture

    if held_keys['7']:
        current_texture = diavolo_texture

    if held_keys['8']:
        current_texture = diobrando_texture

    if held_keys['9']:
        current_texture = kira_texture

    if held_keys['0']:
        current_texture = doski_texture

    if held_keys['right mouse'] or held_keys['left mouse']:
        Hand.active()
    else:
        Hand.passive()


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            scale=1500,
            texture=sky_night_texture,
            doubled_sided=True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            scale=(0.2, 0.3),
            color=color.white,
            texture=hand_texture,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.4)
        )

    def active(self):
        self.position = Vec2(0.1, -0.5)
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.4, -0.4)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            color=color.color(0, 0, 225),
            highlight_color=color.white33
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal, texture=current_texture)
            if key == 'left mouse down':
                destroy(self)


for z in range(15):
    for x in range(15):
        voxel = Voxel((z, 0, x))

player = FirstPersonController()
sky = Sky()
Hand = Hand()
app.run()
