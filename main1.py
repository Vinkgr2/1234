from direct.showbase.ShowBase import ShowBase
 
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        base.disableMouse()
        base.camera.setPos(base.camera, 6, 4, 5)
        base.camera.setHpr(35, 15, 45)
 
game = Game()
game.run()

