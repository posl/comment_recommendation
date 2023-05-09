def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j, A[i], A[j])
            if A[i] % A[j] == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()