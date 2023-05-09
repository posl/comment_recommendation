def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum([A[i]*B[i] for i in range(M)]) + C > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()