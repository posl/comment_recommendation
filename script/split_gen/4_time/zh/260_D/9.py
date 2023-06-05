def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
    ans = [-1]*n
    for i in range(n):
        if ans[i] != -1:
            continue
        x = i
        cnt = 0
        while True:
            cnt += 1
            ans[x] = cnt
            x = p[x]-1
            if ans[x] != -1:
                break
    for i in range(n):
        if ans[i] <= k:
            print(ans[i])
        else:
            print(-1)
