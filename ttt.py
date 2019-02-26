a = int(input())
b = int(input())
c = []
d = []
play = True
while play:   
    for i in range(20):
        for j in range(20):
            for k in range(len(c)):
                if i==c[k] and j==d[k]:
                    print("e", end=' ')
                    break
            else:
                if i==a and j==b:
                    print("P", end=' ')
                else:
                    print("_", end=' ')
        print()
    m = input("Enter move: ")
    print("Enemy is spawned")
    c.append(a+2)
    d.append(b+2) 
    if m=='w':
        a=a-1
    if m=='s':
        a=a+1
    if m=='a':
        b=b-1
    if m=='d':
        b=b+1
    for k in range(len(c)):
        if a==c[k] and b==d[k]:
            play = False
        


        
        
