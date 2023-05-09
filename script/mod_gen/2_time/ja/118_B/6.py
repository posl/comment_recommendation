def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    #print(A)
    ans = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i not in A[j]:
                break
            if j == N - 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()