def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(M):
        ans += (i+1) * A[i]
    print(ans)

if __name__ == '__main__':
    main()