def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    b[m] = c[-1]//a[-1]
    for i in range(m-1,-1,-1):
        b[i] = (c[i]-sum([b[i+j+1]*a[j+1] for j in range(m-i)]))//a[0]
    print(*b)
