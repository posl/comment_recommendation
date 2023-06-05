def main():
    N,M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]
    for i in range(M):
        k,x = map(int, input().split())
        for j in range(k):
            ans[x-1][int(input())-1] = 1
    for i in range(N):
        for j in range(N):
            if ans[i][j] == 0 and i != j:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()