def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    total = sum(A)
    ans = 100000000000000000
    a = 0
    for i in range(N-1):
        a += A[i]
        ans = min(ans, abs(total-a-a))
    print(ans)

if __name__ == '__main__':
    main()