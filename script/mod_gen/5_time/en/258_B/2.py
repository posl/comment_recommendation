def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(8):
                x = i
                y = j
                s = str(a[x][y])
                for l in range(n-1):
                    if k & 1: # up
                        x -= 1
                    if k & 2: # right
                        y += 1
                    if k & 4: # down
                        x += 1
                    s += str(a[x][y])
                ans = max(ans, int(s))
    print(ans)

if __name__ == '__main__':
    main()