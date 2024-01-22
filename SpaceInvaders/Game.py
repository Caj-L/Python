import pygame 

class Player():
    def __init__(self, x = 120, y = 120, width = 400,  height = 240):
        self.x = x
        self.y = y
        self.x_change = 0
        self.color = pygame.Color(0,0,255)
        self.rect = pygame.Rect(self.x,self.y,width,height)

    def update(self,moveCommandX):#,moveCommandY):
        self.x += moveCommandX
        # self.y += moveCommandY

class GameLoop():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.Player = Player()
        self.running = True
        self.moveCommandX = 0
        # self.moveCommandY = 0  

    def processInput(self):
        # self.moveCommandX = 0
        # self.moveCommandY = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.moveCommandX += 8
                elif event.key == pygame.K_LEFT:
                    self.moveCommandX = -8
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moveCommandX = 0
                elif event.key == pygame.K_LEFT:
                    self.moveCommandX = 0
        
    

    def update(self):
        self.Player.update(self.moveCommandX)#,self.moveCommandY)

    def render(self):
        self.window.fill((0,0,0))
        x = self.Player.x
        y = self.Player.y
        pygame.draw.rect(self.window, self.Player.color, self.Player.rect)
        pygame.display.update()   

    def run(self):    
        while self.running:
            self.processInput()
            self.update()
            self.render()        
            self.clock.tick(120)
    
    def exit():
        pygame.quit() 