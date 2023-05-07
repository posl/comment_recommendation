def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()