def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            for k in range(8):
                d = 0
                x = i
                y = j
                while True:
                    if d == n - 1:
                        break
                    if k == 0:
                        x += 1
                    elif k == 1:
                        x -= 1
                    elif k == 2:
                        y += 1
                    elif k == 3:
                        y -= 1
                    elif k == 4:
                        x += 1
                        y += 1
                    elif k == 5:
                        x += 1
                        y -= 1
                    elif k == 6:
                        x -= 1
                        y += 1
                    elif k == 7:
                        x -= 1
                        y -= 1
                    if x < 0 or x >= n or y < 0 or y >= n:
                        break
                    d += 1
                if d == n - 1:
                    num = 0
                    x = i
                    y = j
                    while True:
                        num *= 10
                        num += a[x][y]
                        if k == 0:
                            x += 1
                        elif k == 1:
                            x -= 1
                        elif k == 2:
                            y += 1
                        elif k == 3:
                            y -= 1
                        elif k == 4:
                            x += 1
                            y += 1
                        elif k == 5:
                            x += 1
                            y -= 1
                        elif k == 6:
                            x -= 1
                            y += 1
                        elif k == 7:
                            x -= 1
                            y -= 1
                        if x < 0 or x >= n or y < 0 or y >= n:
                            break
                    ans = max(ans,num)
    print(ans)

if __name__ == '__main__':
    main()