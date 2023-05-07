def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    L = [a[0] for a in A]
    B = [a[1:] for a in A]
    ans = 0
    for b in product(*B):
        p = 1
        for i in range(N):
            p *= b[i]
        if p == X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()