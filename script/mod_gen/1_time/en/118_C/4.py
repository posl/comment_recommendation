def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = A[-1] - 1
    for i in range(N-1):
        ans = min(ans, A[i])
    print(ans)

if __name__ == '__main__':
    main()