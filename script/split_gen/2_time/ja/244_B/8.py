def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 0 # 0:東 1:南 2:西 3:北
    for i in range(n):
        if t[i] == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            else:
                y += 1
        else:
            d = (d + 1) % 4
    print(x, y)
