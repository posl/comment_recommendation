def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    d = 0
    for i in range(n):
        if s[i] == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        else:
            d += 1
            if d == 4:
                d = 0
    print(x, y)
