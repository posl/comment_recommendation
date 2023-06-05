def solve():
    line = input().split()
    S_x = int(line[0])
    S_y = int(line[1])
    G_x = int(line[2])
    G_y = int(line[3])
    x = (G_x*S_y + G_y*S_x)/(S_y + G_y)
    print(x)
