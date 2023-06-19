def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = []
    for i in range(n):
        wall.append(list(map(int,input().split())))
    q = int(input())
    direction = []
    for i in range(q):
        direction.append(list(input().split()))
    for i in range(q):
        if direction[i][0] == "L":
            c = c - int(direction[i][1])
            if c < 1:
                c = 1
        elif direction[i][0] == "R":
            c = c + int(direction[i][1])
            if c > w:
                c = w
        elif direction[i][0] == "U":
            r = r - int(direction[i][1])
            if r < 1:
                r = 1
        elif direction[i][0] == "D":
            r = r + int(direction[i][1])
            if r > h:
                r = h
        if [r,c] in wall:
            if direction[i][0] == "L":
                c = c + int(direction[i][1])
                if c > w:
                    c = w
            elif direction[i][0] == "R":
                c = c - int(direction[i][1])
                if c < 1:
                    c = 1
            elif direction[i][0] == "U":
                r = r + int(direction[i][1])
                if r > h:
                    r = h
            elif direction[i][0] == "D":
                r = r - int(direction[i][1])
                if r < 1:
                    r = 1
        print(r,c)
main()
