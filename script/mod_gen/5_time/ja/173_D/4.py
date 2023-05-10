def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    for i in range(N):
        ans = max(ans, sum(A[i:i+N:2]))
    print(ans)

if __name__ == '__main__':
    main()