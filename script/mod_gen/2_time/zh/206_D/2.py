def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # print(A)
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()