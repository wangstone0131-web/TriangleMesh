from camera import *
from object_3d import *
from projection import *
import pygame as pg


class TriangleRender:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1200,775))
        self.WIDTH,self.HEIGHT = self.screen.get_size()
        self.H_WIDTH,self.H_HEIGHT = self.WIDTH//2,self.HEIGHT//2
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self,[0.5,1,-4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2,0.4,0.2])
        self.object.rotate_y((math.pi/6))

    def draw(self):
        self.screen.fill((pg.Color('darkslategray')))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    app = TriangleRender()
    app.run()