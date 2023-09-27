import pygame


class Gui:
    screen = pygame.display.set_mode([1280, 720])
    dic = {2: 'image\\block\\2.png',
           4: 'image\\block\\4.png',
           8: 'image\\block\\8.png',
           16: 'image\\block\\16.png',
           32: 'image\\block\\32.png',
           64: 'image\\block\\64.png',
           128: 'image\\block\\128.png',
           256: 'image\\block\\256.png',
           512: 'image\\block\\512.png',
           1024: 'image\\block\\1024.png',
           2048: 'image\\block\\2048.png'
           }

    def __init__(self):
        self.running = True
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("2048")
        self.Set.setBackground("image\\2048\\start.jpg")
        self.Set.setMusic('music\\d91pq-08fkg.wav')

    @classmethod
    def font(cls, fonts, pos, color, size=120):
        font = pygame.font.SysFont("Yu Gothic UI Light", size)
        text = font.render(fonts, True, color)
        Gui.screen.blit(text, pos)
        pygame.display.update()

    @classmethod
    def insertImage(cls, imageName, pos):
        image = pygame.image.load(imageName)
        image.convert()
        Gui.screen.blit(image, pos)
        pygame.display.update()

    def refreshScore(self, maxScore, score):
        self.insertImage('image\\gray.png', [286, 98])
        self.insertImage('image\\gray.png', [877, 98])
        fontSize = 80
        if score >= 10000:
            pos1 = 40
            fontSize = 60
        elif score >= 10000:
            pos1 = 45
            fontSize = 70
        elif score >= 100:
            pos1 = 30
        elif score >= 10:
            pos1 = 10
        else:
            pos1 = 0
        if score >= 10000:
            pos2 = 43
            fontSize = 60
        elif maxScore >= 1000:
            pos2 = 38
            fontSize = 70
        elif maxScore >= 100:
            pos2 = 30
        elif score >= 10:
            pos2 = 10
        else:
            pos2 = 0
        self.font(str(score), [320 - pos1, 120], (255, 255, 255), fontSize)
        self.font(str(maxScore), [915 - pos2, 120], (255, 255, 255), fontSize)

    def blockImageInsert(self, Map):
        win = False
        startX = 404
        startY = 221
        px = 470 / Map.size
        Gui.insertImage('image\\graybg.png', (startX, startY))
        cnt = 0
        for i, row in enumerate(Map.map):
            for j, block in enumerate(row):
                bottomPos1 = startX + j * px
                bottomPos2 = startY + i * px
                if block != 0:
                    if block == 2048:
                        win = True
                    cnt += 1
                    image1 = pygame.image.load(Gui.dic[block])
                    image1.convert()
                    blockImage = pygame.transform.scale(image1, (int(px), int(px)))
                    self.screen.blit(blockImage, (bottomPos1, bottomPos2))
        pygame.display.update()
        return win

    class Set:

        @classmethod
        def setBackground(cls, imageName):
            background = pygame.image.load(imageName).convert()
            Gui.screen.blit(background, [0, 0])
            pygame.display.flip()

        @classmethod
        def setMusic(cls, bgm):
            s = pygame.mixer.Sound(bgm)
            s.set_volume(0.5)
            s.play()
