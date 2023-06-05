def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 'E'
    for i in range(n):
        if t[i] == 'S':
            if d == 'E':
                x += 1
            elif d == 'W':
                x -= 1
            elif d == 'N':
                y += 1
            else:
                y -= 1
        else:
            if d == 'E':
                d = 'S'
            elif d == 'W':
                d = 'N'
            elif d == 'N':
                d = 'W'
            else:
                d = 'E'
    print(x, y)
