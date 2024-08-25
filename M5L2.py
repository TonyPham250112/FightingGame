from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (60,60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption("Tony best maze game")
background = transform.scale(image.load("background.png"), (700, 500))

#player = transform.scale(image.load('slime.png'), (100, 100))
player = GameSprite("slime.png", 5, 5, 1)
#enemy = transform.scale(image.load('enemy.png'), (100, 100))
enemy = GameSprite("enemy.png", 100, 100, 2)
#treasure = transform.scale(image.load('treasure.png'), (100, 100))
treasure = GameSprite("treasure.png", 200, 200, 0)


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

is_over = False
clock = time.Clock()
FPS = 60
while not is_over:
    window.blit(background, (0,0))

    player.reset()
    enemy.reset()
    treasure.reset()

    display.update()
    clock.tick(FPS)