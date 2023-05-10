def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # l, r, xを全探索する
    for l in range(N):
        for r in range(l, N):
            for x in range(1, 1001):
                # 条件を満たすかどうか
                ok = True
                for i in range(l, r+1):
                    if A[i] < x:
                        ok = False
                # 条件を満たした場合、ansを更新する
                if ok:
                    ans = max(ans, x*(r-l+1))
    print(ans)

if __name__ == '__main__':
    main()