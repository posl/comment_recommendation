def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 'Yes'
    for i in range(n):
        if i % 2 == 0:
            x -= a[i]
        else:
            x -= a[i]-1
    if x < 0:
        ans = 'No'
    print(ans)
