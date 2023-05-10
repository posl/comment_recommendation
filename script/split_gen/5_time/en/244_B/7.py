def main():
    n = int(input())
    s = input()
    x, y = 0, 0
    for i in range(n):
        if s[i] == 'S':
            if y > 0:
                y -= 1
        else:
            if x == 0:
                if y > 0:
                    y -= 1
                    x += 1
                else:
                    y += 1
            else:
                if y < 0:
                    y += 1
                    x -= 1
                else:
                    y -= 1
    print(x, y)
