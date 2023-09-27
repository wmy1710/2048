import gui
import operate


def restart(Gui):
    Gui.Set.setBackground('image\\2048\\start.jpg')
    size = None
    oriSize = -1
    flag = False
    while True:
        size = operate.startPage(Gui, flag)
        if size == -1:
            break
        elif size == 10:
            break
        else:
            oriSize = size
        Gui.insertImage('image\\color.png', [520, 320])
        Gui.insertImage('image\\color.png', [690, 320])
        Gui.font(str(size), [520, 320], (132, 60, 12))
        Gui.font(str(size), [690, 320], (132, 60, 12))
        flag = True
    if size != -1:
        Gui.Set.setBackground('image\\2048\\22.jpg')
    else:
        oriSize = -1
    return oriSize


def endGame(Gui, Map):
    Gui.Set.setBackground('image\\2048\\3.JPG')
    Gui.font('your score is ' + str(Map.score), [30, 10], (132, 60, 12), 60)
    while True:
        s = operate.re(Gui)
        if s == 'restart':
            Map.setMap(restart(Gui))
            return True
        elif s == 'out':
            return False
        else:
            pass
