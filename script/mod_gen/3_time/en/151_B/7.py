def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = M*N - sum(A)
    if ans <= K and ans >= 0:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()