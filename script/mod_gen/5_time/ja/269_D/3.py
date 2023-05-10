def main():
    n = int(input())
    d = {}
    for i in range(n):
        x, y = map(int, input().split())
        d[(x, y)] = True
    ans = 0
    for k in d:
        x, y = k
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j:
                    continue
                if d.get((x + i, y + j)):
                    ans += 1
                    break
    print(ans // 2)

if __name__ == '__main__':
    main()