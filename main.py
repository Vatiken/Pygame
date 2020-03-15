import pygame

SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second
x =  (WIDTH * 0.45)
y = (HEIGHT * 0.8)
x_change = 0
char_speed = 0

class MySprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(MySprite, self).__init__()

        self.direction = "Right"
        self.width = width
        self.height = height

        self.images = []
        self.images.append(pygame.image.load('images/walk1.png'))
        self.images.append(pygame.image.load('images/walk2.png'))
        self.images.append(pygame.image.load('images/walk3.png'))
        self.images.append(pygame.image.load('images/walk4.png'))
        self.images.append(pygame.image.load('images/walk5.png'))
        self.images.append(pygame.image.load('images/walk6.png'))
        self.images.append(pygame.image.load('images/walk7.png'))
        self.images.append(pygame.image.load('images/walk8.png'))
        self.images.append(pygame.image.load('images/walk9.png'))
        self.images.append(pygame.image.load('images/walk10.png'))

        self.index = 0

        self.image = self.images[self.index]
        self.x = 5
        self.y = 5

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]

        if self.direction == "Left":
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite(150, 198)
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_sprite.x += -5
                my_sprite.direction = "Left"
            elif event.key == pygame.K_RIGHT:
                my_sprite.direction = "Right"
                my_sprite.x += 5
            elif event.key == pygame.K_UP:
                my_sprite.y -= 5
            elif event.key == pygame.K_DOWN:
                my_sprite.y += 5
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()