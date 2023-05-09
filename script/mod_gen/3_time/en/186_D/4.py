def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        ans += i * A[i] - (N - i - 1) * A[i]
    print(ans)

if __name__ == '__main__':
    main()