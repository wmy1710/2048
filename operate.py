import pygame

import gui


def startPage(Gui, flag):
    while True:
        for event in pygame.event.get():
            num = 0
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                Gui.running = False
                return -1
            elif keys_pressed[pygame.K_2]:
                num = 2
            elif keys_pressed[pygame.K_3]:
                num = 3
            elif keys_pressed[pygame.K_4]:
                num = 4
            elif keys_pressed[pygame.K_5]:
                num = 5
            elif keys_pressed[pygame.K_6]:
                num = 6
            elif keys_pressed[pygame.K_7]:
                num = 7
            elif keys_pressed[pygame.K_8]:
                num = 8
            elif keys_pressed[pygame.K_9]:
                num = 9
            elif keys_pressed[pygame.K_SPACE] and flag == True:
                num = 10
            else:
                continue
            return num


def wasd(Gui):
    while True:
        for event in pygame.event.get():
            op = ''
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                Gui.running = False
                op = 'out'
            elif keys_pressed[pygame.K_w]:
                op = 'w'
            elif keys_pressed[pygame.K_a]:
                op = 'a'
            elif keys_pressed[pygame.K_s]:
                op = 's'
            elif keys_pressed[pygame.K_d]:
                op = 'd'
            elif keys_pressed[pygame.K_RETURN]:
                op = 'restart'
            else:
                continue
            Gui.Set.setMusic('music\\short.wav')
            return op


def re(Gui):
    while True:
        for event in pygame.event.get():
            print(pygame.mouse.get_pressed())
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                Gui.running = False
                return 'out'
            elif keys_pressed[pygame.K_RETURN]:
                return 'restart'
            elif pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                if (287 <= x <= 492) and (404 <= y <= 506):
                    print('test1')
                    return 'restart'
                elif (784 <= x <= 990) and (407 <= y <= 507):
                    Gui.running = False
                    return 'out'
            else:
                continue


def win(Gui):
    while True:
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                Gui.running = False
                return 'out'
            elif keys_pressed[pygame.K_SPACE]:
                return 'restart'
            else:
                continue


