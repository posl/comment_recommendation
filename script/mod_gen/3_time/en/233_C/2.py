def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 2**N):
        bit = bin(i)[2:].zfill(N)
        cnt = 1
        for j in range(N):
            if bit[j] == '1':
                cnt *= L[j][1+bit.count('1')]
        if cnt == X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()