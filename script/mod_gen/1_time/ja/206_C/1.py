def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i-1] != A[i]:
            ans += N - i - 1
    print(ans)

if __name__ == '__main__':
    main()