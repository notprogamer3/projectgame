import os
import random
import sys

import pygame

bulletsp = {(154, 767): True, (125, 767): True, (93, 767): True}
points = {(370, 795): False, (400, 795): False,
          (428, 795): False, (459, 795): False, (487, 795): False,
          (516, 795): False, (546, 795): False,
          (577, 795): False, (604, 795): False, (635, 795): False}
a13 = list(bulletsp.values())
nowb = 0
keys = list(points.keys())
keys2 = list(bulletsp.keys())
testcyc = 0
now1 = 0
shoot1 = False


def load_image(name, path, colorkey=None):
    fullname = os.path.join(path, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey == -1:
        image.set_colorkey('black')
    if colorkey == -2:
        image.set_colorkey('white')
    return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def start():
    global bulletsp
    global a13
    global nowb
    global now1
    nowb = 0
    a13 = bulletsp.keys()
    for i in a13:
        bulletsp[i] = True
    if now1 != 10:
        spy = 0
        spx = 0
        while spy == 0:
            spy = random.randrange(-20, 20)
        while spx == 0:
            spx = random.randrange(-20, 20)
        coll = random.randrange(3, 10)
        starty = random.randrange(350)
        Bomb(width - 150, starty, spx, spy, coll, all_sprites)
        Bomb(0, 1, 5, 5, 6, all_sprites)
    elif now1 == 10:
        finall.final()


def wastedbullets():
    global bulletsp
    global keys2
    cuting = pygame.rect.Rect(154, 767, 20, 35)
    cuting.copy()
    for i in keys2:
        if not bulletsp[i]:
            x1, y1 = i
            pygame.draw.rect(screen, pygame.Color((30, 17, 17)), (x1, y1, 22, 35))


def kiledducks():
    global points
    global keys
    for i in keys:
        if points[i]:
            pygame.draw.circle(screen, pygame.Color('green'), i, 7)
        else:
            pygame.draw.circle(screen, pygame.Color('red'), i, 7)


class Bomb(pygame.sprite.Sprite):
    image7 = load_image("kill2.png", 'data', colorkey=-1)
    image6 = load_image("falling2.png", 'data', colorkey=-1)
    image2 = load_image('moveleft2.png', 'data', colorkey=-1)
    image3 = load_image('movelefttop2.png', 'data', colorkey=-1)
    image4 = load_image('moveright2.png', 'data', colorkey=-1)
    image5 = load_image('moverigtop2.png', 'data', colorkey=-1)

    def __init__(self, x2, y2, x1, y1, colt, *group):
        super().__init__(*group)
        self.x1 = x1
        self.y1 = y1
        self.image = self.image7
        self.colt = colt
        self.live = True
        self.add(bombs)
        self.rect = self.image.get_rect()
        self.changeimg()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x2
        self.rect.y = y2
        self.count = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        global shoot
        global now1
        global nowb
        global bulletsp
        global a13
        global testcyc
        if not self.live:
            if self.count == 10:
                self.rect.y += 10
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                if self.rect.y > 505:
                    points[keys[now1]] = True
                    testcyc += 1
                    now1 += 1
                    self.kill()
            elif self.count == 0:
                x3 = self.rect.x
                y3 = self.rect.y
                self.image = self.image7
                self.rect.x = x3
                self.rect.y = y3
                self.count += 1
            else:
                self.count += 1
        elif self.rect.x > width or self.rect.x < -100:
            testcyc += 1
            now1 += 1
            self.kill()
        else:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.rect.x += self.x1
            self.rect.y += self.y1
            if self.rect.x < 0 and self.colt != 0:
                self.x1 = self.x1 * -1
                self.colt -= 1
                self.changeimg()
            if self.rect.x > 860 and self.colt != 0:
                self.x1 = self.x1 * -1
                self.colt -= 1
                self.changeimg()
            if self.rect.y < 0:
                self.y1 = self.y1 * -1
                self.changeimg()
            if self.rect.y > 400:
                self.y1 = self.y1 * -1
                self.changeimg()

    def changeimg(self):
        if self.x1 >= 0 and self.y1 >= 0:
            x3 = self.rect.x
            y3 = self.rect.y
            self.frames = []
            self.cut_sheet(self.image4, 3, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x3
            self.rect.y = y3
        elif self.x1 <= 0 and self.y1 >= 0:
            x3 = self.rect.x
            y3 = self.rect.y
            self.frames = []
            self.cut_sheet(self.image2, 3, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x3
            self.rect.y = y3
        elif self.x1 <= 0 and self.y1 < 0:
            x3 = self.rect.x
            y3 = self.rect.y
            self.frames = []
            self.cut_sheet(self.image3, 3, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x3
            self.rect.y = y3
        elif self.x1 >= 0 and self.y1 < 0:
            x3 = self.rect.x
            y3 = self.rect.y
            self.frames = []
            self.cut_sheet(self.image5, 3, 1)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x3
            self.rect.y = y3

    def checkdeath(self):
        self.live = False
        x3 = self.rect.x
        y3 = self.rect.y
        self.frames = []
        self.cut_sheet(self.image6, 4, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x3
        self.rect.y = y3
        try:
            death.play()
        except Exception:
            pass


class Mainscreen(pygame.sprite.Sprite):
    image = load_image("main2.png", 'data')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Mainscreen.image
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = -5

    def update(self):
        pass


class Fin(pygame.sprite.Sprite):
    image1 = load_image('lost.png', 'data', colorkey=-1)
    image2 = load_image('won.png', 'data', colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x = -200

    def update(self):
        pass

    def final(self):
        global points
        global keys
        win = True
        for i in keys:
            if not points[i]:
                win = False
        if win:
            self.image = Fin.image2
            self.rect = self.image.get_rect()
            self.rect.x = 300
            self.rect.y = 300
        else:
            self.image = Fin.image1
            self.rect = self.image.get_rect()
            self.rect.x = 300
            self.rect.y = 300


class Bullet(pygame.sprite.Sprite):
    image = load_image('point3.png', 'data', colorkey=-2)

    def __init__(self, *group):
        super().__init__(*group)
        x, y = pygame.mouse.get_pos()
        self.add(bullet)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x + 12
        self.rect.y = y + 12
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        x, y = pygame.mouse.get_pos()
        if x <= width - 35 and y <= height - 35:
            self.rect.x = x + 12
            self.rect.y = y + 12
        global a13
        global testcyc
        global lasttest
        global shoot1
        global bulletsp
        global nowb
        a13 = list(bulletsp.values())
        if True in a13 and not lasttest and shoot1:
            a = pygame.sprite.spritecollideany(self, bombs)
            if a:
                if pygame.sprite.collide_mask(self, a):
                    shoot1 = False
                    a.checkdeath()
                    bulletsp[keys2[nowb]] = False
                    nowb += 1
                else:
                    shoot1 = False
                    bulletsp[keys2[nowb]] = False
                    nowb += 1
            else:
                shoot1 = False
                bulletsp[keys2[nowb]] = False
                nowb += 1


class Crosshair(pygame.sprite.Sprite):
    image1 = load_image("crosshair.png", 'data', colorkey=-2)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pygame.mouse.get_pos()
        self.add(bullet)

    def update(self):
        x, y = pygame.mouse.get_pos()
        if x >= 0 and y >= 0 and x <= width - 35 and y <= height - 35:
            self.rect.x, self.rect.y = pygame.mouse.get_pos()


class Restart(pygame.sprite.Sprite):
    image1 = load_image("restart3.png", 'data', colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = 705
        self.rect.y = 766

    def update(self):
        pass


class Dogg(pygame.sprite.Sprite):
    image1 = load_image("2duck1.png", 'data', colorkey=-1)
    image2 = load_image("1duck.png", 'data', colorkey=-1)
    image3 = load_image("laugh1.png", 'data', colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = -200

    def show(self):
        global points
        global keys
        global now1
        x1 = now1 - 1
        x2 = now1 - 2
        if points[keys[x1]] and points[keys[x2]]:
            self.image = Dogg.image1
            self.rect.x = 400
            self.rect.y = 470
        elif points[keys[x1]] and not points[keys[x2]] or not points[keys[x1]] and points[keys[x2]]:
            self.image = Dogg.image2
            self.rect.x = 400
            self.rect.y = 480
        else:
            self.image = Dogg.image3
            self.rect.x = 400
            self.rect.y = 470

    def hide(self):
        self.rect.x = -200

    def update(self):
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('круг')
    size = width, height = 956, 894
    screen = pygame.display.set_mode(size)

    v = 20
    try:
        death = pygame.mixer.Sound('data/death.mp3')
    except Exception:
        pass
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True
    screen.fill('blue')
    bombs = pygame.sprite.Group()
    bullet = pygame.sprite.Group()
    Mainscreen(all_sprites)
    Restart(all_sprites)
    dragon = AnimatedSprite(load_image("dog3.png", 'data', colorkey=-1), 5, 1, 0, 630)
    all_sprites.draw(screen)
    pygame.mouse.set_visible(False)
    shoot = False
    jump = True
    lasttest = True
    times = 0
    cycle = True
    times1 = 0
    finall = Fin(all_sprites)
    dog = Dogg(all_sprites)
    a1 = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not lasttest:
                shoot = True
                shoot1 = True
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if key[pygame.K_r]:
                    bulletsp = {(154, 767): True, (125, 767): True, (93, 767): True}
                    points = {(370, 795): False, (400, 795): False,
                              (428, 795): False, (459, 795): False, (487, 795): False,
                              (516, 795): False, (546, 795): False,
                              (577, 795): False, (604, 795): False, (635, 795): False}
                    a13 = list(bulletsp.values())
                    nowb = 0
                    keys = list(points.keys())
                    keys2 = list(bulletsp.keys())
                    testcyc = 0
                    now1 = 0
                    shoot1 = False
                    all_sprites = pygame.sprite.Group()
                    bombs = pygame.sprite.Group()
                    bullet = pygame.sprite.Group()
                    Mainscreen(all_sprites)
                    Restart(all_sprites)
                    dragon = AnimatedSprite(load_image("dog3.png", 'data', colorkey=-1), 5, 1, 0, 630)
                    all_sprites.draw(screen)
                    shoot = False
                    jump = True
                    lasttest = True
                    times = 0
                    cycle = True
                    times1 = 0
                    finall = Fin(all_sprites)
                    dog = Dogg(all_sprites)
                    a1 = pygame.time.Clock()
                    a50 = 0
        a1.tick(v)
        if dragon.rect.x != 400:
            dragon.rect.x += 5
        if times == 3:
            dragon.kill()
            lasttest = False
            times = 4
        if dragon.rect.x == 400 and jump:
            jump = False
            a4 = dragon.rect.x
            times += 1
            dragon.kill()
            dragon = AnimatedSprite(load_image("jump2.png", 'data', colorkey=-1), 3, 1, a4, 600)
        if times != 0 and lasttest:
            times += 1
        pygame.display.flip()
        screen.fill('blue')
        all_sprites.update()
        all_sprites.draw(screen)
        if not lasttest:
            kiledducks()
            wastedbullets()
            bullet.draw(screen)
        if not lasttest and cycle and times1 == 0:
            dog.hide()
            cycle = False
            start()
            Crosshair(all_sprites)
            Bullet(all_sprites)
        if testcyc == 2:
            cycle = True
            testcyc = 0
            times1 = 15
            dog.show()
        if times1 != 0:
            times1 -= 1
    pygame.quit()
