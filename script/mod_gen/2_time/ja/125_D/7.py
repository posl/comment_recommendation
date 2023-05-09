def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    if N%2 == 0:
        B = [abs(A[i]) for i in range(N) if i%2 == 1]
        ans -= 2*min(B)
    print(ans)

if __name__ == '__main__':
    main()