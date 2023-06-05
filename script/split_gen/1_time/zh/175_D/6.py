def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    p = [p[i]-1 for i in range(n)]
    ans = -float("inf")
    for i in range(n):
        now = i
        tmp = 0
        cnt = 0
        while True:
            cnt += 1
            tmp += c[p[now]]
            now = p[now]
            ans = max(ans,tmp)
            if cnt == k:
                break
            if now == i:
                break
    print(ans)
