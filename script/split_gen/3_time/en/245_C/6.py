def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = [0]*n
    for i in range(n):
        if i == 0:
            x[i] = min(a[i],b[i])
        else:
            x[i] = min(a[i],b[i])
            if abs(x[i]-x[i-1]) > k:
                x[i] = max(a[i],b[i])
                if abs(x[i]-x[i-1]) > k:
                    print("No")
                    return
    print("Yes")
    return
