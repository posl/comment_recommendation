def main():
    n, m = map(int, input().split())
    cake = []
    for _ in range(n):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**3):
        tmp = []
        for j in range(n):
            tmp.append(sum([cake[j][k] if (i >> k) & 1 else -cake[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

if __name__ == '__main__':
    main()