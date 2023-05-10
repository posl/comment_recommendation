def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i]-b)
    print(ans)
    return

if __name__ == '__main__':
    main()