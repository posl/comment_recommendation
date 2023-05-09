def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2**N):
        b = bin(i)[2:].zfill(N)
        p = 1
        for j in range(N):
            if b[j] == '1':
                p *= L[j][1]
            else:
                p *= L[j][2]
        if p == X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()