def main():
    N = int(input())
    ans = []
    for i in range(N):
        ans.append([1]*(i+1))
        for j in range(1,i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    for i in range(N):
        print(*ans[i])
main()

if __name__ == '__main__':
    main()