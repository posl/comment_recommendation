def main():
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a = list(set(a))
    ans = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            for k in range(j,len(a)):
                if a[i]+a[j]+a[k]<=w:
                    ans += 1
    print(ans)
