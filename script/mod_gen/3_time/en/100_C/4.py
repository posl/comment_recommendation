def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()