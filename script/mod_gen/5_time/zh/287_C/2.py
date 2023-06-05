def main():
    n,m = map(int,input().split())
    u = [0] * m
    v = [0] * m
    for i in range(m):
        u[i],v[i] = map(int,input().split())
    ans = 'Yes'
    for i in range(m):
        if u[i] > v[i]:
            u[i],v[i] = v[i],u[i]
    for i in range(1,n+1):
        if u.count(i) > 1:
            ans = 'No'
            break
    if ans == 'Yes':
        for i in range(m-1):
            if v[i] != u[i+1]:
                ans = 'No'
                break
    print(ans)

if __name__ == '__main__':
    main()