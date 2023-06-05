def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        if k > 0:
            sum += max(a[i] - x,0)
            k -= 1
        else:
            sum += a[i]
    print(sum)
