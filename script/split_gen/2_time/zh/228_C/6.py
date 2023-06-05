def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    b = [0 for i in range(n+1)]
    b[x] = 1
    cnt = 1
    for i in range(1,n+1):
        if b[a[i]] == 0:
            b[a[i]] = 1
            cnt += 1
    print(cnt)
