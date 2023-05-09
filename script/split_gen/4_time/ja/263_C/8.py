def main():
    n,m = map(int,input().split())
    a = []
    for i in range(1,m+1):
        a.append(i)
    for i in range(1,n):
        a.append(a[-1]+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(a[j-1],end="")
            if j==n:
                print()
            else:
                print(" ",end="")
        a[-j] += 1
        for k in range(n-1):
            if a[-j+k] == m+1:
                a[-j+k] = 1
                a[-j+k+1] += 1
    return 0
