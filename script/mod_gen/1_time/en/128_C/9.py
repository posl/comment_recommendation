def main():
    N, M = map(int, input().split())
    bulbs = []
    for _ in range(M):
        bulbs.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        on = [False] * N
        for j in range(N):
            if ((i >> j) & 1):
                on[j] = True
        ok = True
        for j in range(M):
            count = 0
            for k in bulbs[j][1:]:
                if on[k-1]:
                    count += 1
            if count % 2 != p[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()