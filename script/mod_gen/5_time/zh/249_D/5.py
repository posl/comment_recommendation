def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if j == k:
                    continue
                if A[j] % A[k] != 0:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()