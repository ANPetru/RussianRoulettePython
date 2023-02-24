from random import randrange


class Person:
    def __init__(self, name):
        self.name = name
        self.alive = True


players = [Person("Alex"), Person("Mat"), Person("Julia"), Person("Luis")]
chamber = [1, 2, 3, 4, 5, 6]
bullet = randrange(1, 7)
currentPlayer = 0
gameOver = False


def displayChamber():
    print("Chamber:", end="")
    for b in chamber:
        if b == -1:
            print(" _ ", end="")
        else:
            print("", b, "", end="")
    print("")


def displayPlayers():
    for player in players:
        if player.alive:
            print(player.name, "\033[92mis alive\033[0m")
        else:
            print(player.name, "\033[91mis dead\033[0m")


def getRandomBullet():
    rb = 0
    hit = True
    while hit:
        hit = False
        rb = randrange(0, 6)
        if chamber[rb] == -1:
            hit = True
    return rb


def setNextPlayer():
    global currentPlayer
    currentPlayer += 1
    if currentPlayer >= len(players):
        currentPlayer = 0
    while not players[currentPlayer].alive:
        setNextPlayer()


def resetChamber():
    global chamber
    global bullet
    chamber = [1, 2, 3, 4, 5, 6]
    bullet = randrange(1, 7)


def shot():
    global currentPlayer
    randomBullet = getRandomBullet()
    print("Shooting...", chamber[randomBullet])
    if chamber[randomBullet] == bullet:
        players[currentPlayer].alive = False
        resetChamber()
    else:
        chamber[randomBullet] = -1

    setNextPlayer()


def checkEndGame():
    global gameOver
    winner = ""
    playersAlive = 0
    for player in players:
        if player.alive:
            winner = player.name
            playersAlive += 1

    if playersAlive == 1:
        print(winner, "WON THE GAME!!!!")
        gameOver = True


while not gameOver:
    displayChamber()
    displayPlayers()
    print(players[currentPlayer].name, "'s turn")
    cont = input("Continue?y/n").lower()
    if cont == "y":
        shot()
        checkEndGame()
    elif cont == "n":
        gameOver = True
displayPlayers()
