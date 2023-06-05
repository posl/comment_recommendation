def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = []
    for i in range(n):
        wall.append(list(map(int,input().split())))
    q = int(input())
    order = []
    for i in range(q):
        order.append(list(map(str,input().split())))
    #print(order)
    #print(wall)
    #print(order[0][0])
    #print(order[0][1])
    #print(order[1][0])
    #print(order[1][1])
    #print(order[2][0])
    #print(order[2][1])
    #print(order[3][0])
    #print(order[3][1])
    #print(order[4][0])
    #print(order[4][1])
    #print(order[5][0])
    #print(order[5][1])
    #print(order[6][0])
    #print(order[6][1])
    #print(order[7][0])
    #print(order[7][1])
    #print(order[8][0])
    #print(order[8][1])
    #print(order[9][0])
    #print(order[9][1])
    #print(order[10][0])
    #print(order[10][1])
    r = r - 1
    c = c - 1
    for i in range(q):
        if order[i][0] == 'L':
            for j in range(int(order[i][1])):
                if c - 1 >= 0:
                    if [r,c-1] in wall:
                        pass
                    else:
                        c = c - 1
        elif order[i][0] == 'R':
            for j in range(int(order[i][1])):
                if c + 1 <= w:
                    if [r,c+1] in wall:
                        pass
                    else:
                        c = c + 1
        elif order[i][0] == 'U':
            for j in range(int(order[i][1])):
                if r - 1 >= 0:
                    if [r-1,c] in wall:
                        pass
                    else:
                        r = r - 1
        elif order[i][0] == 'D':
            for j in range(int(order[i][1])):
                if r + 1 <= h
