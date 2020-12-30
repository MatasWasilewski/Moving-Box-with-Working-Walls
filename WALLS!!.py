import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
screen_width = 1000
screen_height = 650
size = [screen_width,screen_height]


#classes


class Player(pygame.sprite.Sprite):


    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.Surface([15,15])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self,x,y):

        self.change_x += x
        self.change_y += y

    def update(self):

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self,self.walls,False)

        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right


        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self,self.walls,False)

        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

#class for wall

class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):

        super().__init__()


        self.image = pygame.Surface([width,height])
        self.image.fill(blue)


        self.rect = self.image.get_rect()

        self.rect.y = y
        self.rect.x = x


pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze Runner")

clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None,25)

all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()


#wall building

wall = Wall(0,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall2 = Wall(10,0,790,10)
wall_list.add(wall2)
all_sprite_list.add(wall2)

wall3 = Wall(10,200,500,10)
wall_list.add(wall3)
all_sprite_list.add(wall3)

player = Player(50,50)
player.walls = wall_list
all_sprite_list.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,-3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,-3)

    all_sprite_list.update()
     
    screen.fill(black)
    all_sprite_list.draw(screen)
    
    text= font.render("© Game by Matas and Alan",True,white)
    screen.blit(text,[750,25])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
