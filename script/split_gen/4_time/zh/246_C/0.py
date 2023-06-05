def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if k > 0:
            count += min(a[i],x)
            k -= 1
        else:
            count += a[i]
    print(count)
