class Person:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.display = "P"
        self.die = False

    def move(self, inp):
        if inp == "w":
            self.y -= 1
        elif inp == "s":
            self.y += 1
        elif inp == "a":
            self.x -= 1
        elif inp == "d":
            self.x += 1
        else:
            return False
        return True

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.display = "E"

    def kill(self, player):
        if self.x == player.x and self.y == player.y:
            player.die = True

class Map:

    def __init__(self, player, enemies, w, blank):
        self.player = player
        self.enemies = enemies
        self.blank = blank
        self.w = w

    def render(self):
        for y in range(self.w):
            for x in range(self.w):
                for one in self.enemies:
                    if x == one.x and y == one.y:
                        print(one.display, end=' ')
                        break
                else:
                    if x == self.player.x and y == self.player.y:
                        print(self.player.display, end=' ')
                    else:
                        print(self.blank, end=' ')
            print()

    def increase(self):
        self.w += 1

def gameplay():
    player = Person(3, 4)
    enemies = []
    map1 = Map(player, enemies, 10, "_")
    play = True
    while play:
        if player.die:
            print("You've dead!")
            play = False
        else:
            map1.render()

            validate = True
            while validate:
                inp = input("Enter move: ")
                valid = player.move(inp)
                if valid:
                    validate = False
                else:
                    print("Invalid input!")
            for enemy in enemies:
                enemy.kill(player)
            enemies.append(Enemy(player.x + 2, player.y + 2))
            
if __name__ == "__main__":
    gameplay()

##minh = Person(2, 3)
##
##print(minh.x)
##print(minh.display)
##
##minh.move("d")
##
##print(minh.x)

##p = [3, 5]
##e = []
##play = True
##while play:   
##    for i in range(20):
##        for j in range(20):
##            for k in range(len(e)):
##                if i==e[k][0] and j==e[k][1]:
##                    print("e", end=' ')
##                    break
##            else:
##                if i==p[0] and j==p[1]:
##                    print("P", end=' ')
##                else:
##                    print("_", end=' ')
##        print()
##    m = input("Enter move: ")
##    print("Enemy is spawned")
##    e.append([p[0] + 2, p[1] + 2])
##    if m=='w':
##        p[0] = p[0] - 1
##    if m=='s':
##        p[0] = p[0] + 1
##    if m=='a':
##        p[1] = p[1] - 1
##    if m=='d':
##        p[1] = p[1] + 1
##    for k in range(len(e)):
##        if p[0]==e[k][0] and p[1]==e[k][1]:
##            play = False
