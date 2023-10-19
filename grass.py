from pico2d import load_image

import game_world


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 60)

    def update(self):
        pass


class Grass2:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,80)

    def update(self):
        pass
