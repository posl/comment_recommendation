def main():
    n,x,y = map(int, input().split())
    u = [0] * (n-1)
    v = [0] * (n-1)
    for i in range(n-1):
        u[i],v[i] = map(int, input().split())
    #print(n,x,y,u,v)
    ans = []
    for i in range(n-1):
        for j in range(i+1,n):
            #print(i,j)
            if i == x-1 and j == y-1:
                ans.append(i+1)
                ans.append(j+1)
                continue
            if i == y-1 and j == x-1:
                ans.append(i+1)
                ans.append(j+1)
                continue
            if i == j:
                continue
            if i == x-1:
                if j in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if i == y-1:
                if j in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if j == x-1:
                if i in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if j == y-1:
                if i in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if u[i] == u[j]:
                ans.append(u[i])
                ans.append(v[i])
                ans.append(v[j])
                continue
            if u[i] == v[j]:
                ans.append(u[i])
                ans.append(v[i])
                ans.append(u[j])
                continue
            if v[i] == u[j]:
                ans.append(v[i])
                ans.append(u[i])
                ans.append(v[j])
                continue
            if v[i] == v[j]:
                ans.append(v[i])
                ans.append(u[i])
                ans.append(u[j])
                continue
    #print(ans)
    print(*ans)

if __name__ == '__main__':
    main()