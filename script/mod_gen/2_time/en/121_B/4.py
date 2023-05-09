def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for a in A:
        if sum([a[i] * B[i] for i in range(M)]) + C > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()