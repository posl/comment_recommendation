def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] != A[N-1-i]:
            ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()