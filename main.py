import random

import gui
import map
import operate
import systemFunc

Map = map.Map()
Gui = gui.Gui()
while Gui.running:
    size = systemFunc.restart(Gui)
    if size == -1:
        break
    Map.setMap(size)
    maxScore = 0
    oriMap = [[0 for i in range(size+1)] for j in range(size+1)]
    while True:
        if Map.same(oriMap):
            Map.add(random.randint(1, (Map.size * Map.size) - Map.getCnt()))
        oriMap = Map.copyMap()
        win = Gui.blockImageInsert(Map)
        if maxScore < Map.score:
            maxScore = Map.score
        Gui.refreshScore(maxScore, Map.score)
        if win:
            Gui.font('Success', [200, 200], (132, 60, 12), 300)
            Gui.font('Press space to continue.....', [210, 400], (132, 60, 12), 30)
            s = operate.win(Gui)
            if s == 'restart':
                if not systemFunc.endGame(Gui, Map):
                    break
                else:
                    continue
            else:
                break
        op = operate.wasd(Gui)
        if op == 'out':
            break
        elif op == 'restart':
            Map.setMap(systemFunc.restart(Gui))
            continue
        else:
            Map.operate(op)
        if Map.getCnt() == Map.size * Map.size:
            if not systemFunc.endGame(Gui, Map):
                break
