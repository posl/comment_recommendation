def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    dir = 0
    for c in T:
        if c == 'S':
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        elif c == 'R':
            dir += 1
            if dir > 3:
                dir = 0
    print(x, y)
