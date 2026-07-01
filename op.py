import pyautogui as pag
import pydirectinput as pdi
import pygetwindow as pgw
import time

onJA = True

def getISATWindow():
    window = pgw.getWindowsWithTitle("IN STARS AND TIME v1.0.6.3")[0]
    return window.topleft, window.bottomright

print("Please focus on the ISAT Window. Do not move the window.")
time.sleep(2)
topLeft, bottomRight = getISATWindow()
print(f"Window detected at coordinates {topLeft} and {bottomRight}")
ISATregion = (topLeft.x, topLeft.y, bottomRight.x, bottomRight.y)

def waitFightStart():
    pdi.keyDown("escape")
    while pag.locateOnScreen('escape.png', region=ISATregion) == None: pass
    print("Escape seen")
    pdi.keyUp("escape")
    pdi.press('z')

def inFight():
    return pag.locateOnScreen('odile.png', region=ISATregion)

def justAttack():
    # enter craft menu
    temp = onJA
    print("First attack")
    pdi.press('z')
    if not temp:
        pdi.press('z')
        pdi.press(['down','right'])
        temp = True
    pdi.press(['z','z','z','z'],interval=0.1)
    return temp

def tripAttack():
    print("Second attack")
    pdi.press('z')
    pdi.press(['up','left'])
    pdi.press(['z','z','z','z'],interval=0.1)
    return False

while True:
    #refresh room and get into position
    pdi.press('right')
    time.sleep(0.7)
    pdi.keyDown('left')
    time.sleep(1)
    pdi.keyUp('left')

    #wait for a fight to occur + animations
    time.sleep(3)
    waitFightStart()

    #attack with Just Attack
    print(f'attacking, Just Attack? = {onJA}')
    onJA = justAttack()

    #make sure that animations have finished
    time.sleep(5)

    #check if still in fight
    if inFight():
        #enemy not killed, let mira guard
        pdi.press('z',presses=3)
        time.sleep(2)
        if inFight():
            #turn back to Siffrin
            pdi.press('z',presses=3)
            time.sleep(2)
            print(f'attacking, Just Attack? = {onJA}')
            #since the triple attack was chosen, the default is no longer Just Attack
            tripAttack()
            onJA = False
    #fight is over, triple attack not procced so onJA is untouched
    #wait for all dialogues to finish
    pdi.keyDown('z')
    time.sleep(5)
    
    #return to position
    time.sleep(0.8)
    pdi.press('right',presses=3)