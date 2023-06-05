def main():
    h,w,rs,cs = map(int,input().split())
    n = int(input())
    walls = []
    for i in range(n):
        walls.append(list(map(int,input().split())))
    q = int(input())
    commands = []
    for i in range(q):
        commands.append(list(input().split()))
    #print(h,w,rs,cs)
    #print(n)
    #print(walls)
    #print(q)
    #print(commands)
    #判断当前位置是否有墙
    def isWall(x,y):
        if [x,y] in walls:
            return True
        else:
            return False
    #判断当前位置是否在网格内
    def isInner(x,y):
        if x>=1 and x<=h and y>=1 and y<=w:
            return True
        else:
            return False
    #高桥移动
    def move(x,y,direction):
        if direction=='L':
            y -= 1
        elif direction=='R':
            y += 1
        elif direction=='U':
            x -= 1
        elif direction=='D':
            x += 1
        else:
            print('error')
        return x,y
    #高桥移动一次
    def moveOnce(x,y,direction):
        x,y = move(x,y,direction)
        if isInner(x,y) and not isWall(x,y):
            return x,y
        else:
            return x,y
    #高桥移动多次
    def moveMultiTimes(x,y,direction,times):
        for i in range(times):
            x,y = moveOnce(x,y,direction)
        return x,y
    #高桥移动多次，直到遇到墙
    def moveUntilWall(x,y,direction):
        while True:
            if isInner(x,y) and not isWall(x,y):
                x,y = moveOnce(x,y,direction)
            else:
                break
        return x,y
    #高桥移动多次，直到遇到墙或者网格边界
    def moveUntilWallOrBorder(x,y,direction):
        while True:
            if isInner(x,y) and not isWall(x,y):
                x,y = moveOnce(x,y,direction)
            else:
