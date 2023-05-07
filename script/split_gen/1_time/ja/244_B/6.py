def main():
    N = int(input())
    T = input()
    x,y = 0,0
    d = 0
    for t in T:
        if t == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            else:
                y += 1
        else:
            d = (d+1)%4
    print(x,y)
