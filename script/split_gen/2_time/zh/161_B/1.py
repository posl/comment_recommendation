def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    for i in range(m,n):
        if a[i] < sum/(4*m):
            print("否")
            return
    print("是")
    return
