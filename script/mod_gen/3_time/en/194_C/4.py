def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, N):
        ans += (i * A[i] - sum(A[:i])) ** 2
    print(ans)

if __name__ == '__main__':
    main()