def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort(key=lambda x:x[0])
    AB.sort(key=lambda x:x[1],reverse=True)
    ans = 0
    for i in range(M):
        ans += AB[i][1]
    print(ans)

if __name__ == '__main__':
    main()