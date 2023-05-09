def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    if N == 2:
        print(ans)
        return
    for i in range(N-2):
        ans += abs(A[i] - A[i+1])
    ans += abs(A[N-2])
    print(ans)

if __name__ == '__main__':
    main()