def main():
    N,M = map(int,input().split())
    u = [0]*M
    v = [0]*M
    for i in range(M):
        u[i],v[i] = map(int,input().split())
    ans = 0
    for i in range(M):
        for j in range(i+1,M):
            if u[i] == u[j] or u[i] == v[j] or v[i] == u[j] or v[i] == v[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()