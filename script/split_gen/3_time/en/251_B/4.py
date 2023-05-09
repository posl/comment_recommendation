def main():
    import sys
    input = sys.stdin.readline
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] > w:
            break
        ans += 1
        for j in range(i+1,n):
            if a[i] + a[j] > w:
                break
            ans += 1
            for k in range(j+1,n):
                if a[i] + a[j] + a[k] > w:
                    break
                ans += 1
    print(ans)
