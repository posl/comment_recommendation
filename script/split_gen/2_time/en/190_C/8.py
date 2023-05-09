def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    k = int(input())
    c = []
    d = []
    for i in range(k):
        c.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**k):
        dish = [0] * (n+1)
        for j in range(k):
            if ((i>>j) & 1):
                dish[c[j][0]] += 1
            else:
                dish[c[j][1]] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j][0]] >= 1 and dish[a[j][1]] >= 1:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
