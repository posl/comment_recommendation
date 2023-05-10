def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        count = 0
        for j in range(N):
            if A[j] & (1 << i):
                count += 1
        ans += (1 << i) * (N - count) * count
    print(ans)
main()

if __name__ == '__main__':
    main()