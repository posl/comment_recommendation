def main():
    n,m = map(int,input().split())
    if m == 0:
        print(3)
        return
    # 都市を通る道路のリスト
    cities = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        cities[a-1].add(b-1)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i in cities[j]:
                continue
            for k in range(n):
                if i == k:
                    continue
                if j == k:
                    continue
                if i in cities[k]:
                    continue
                if j in cities[k]:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()