def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #print(N, X)
    #print(AB)
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        #print(ans)
    ans += min(AB[i][1] for i in range(N))
    #print(ans)
    print(ans + X)

if __name__ == '__main__':
    main()