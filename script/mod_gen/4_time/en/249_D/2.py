def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] % A[j] == 0:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()