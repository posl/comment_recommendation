def main():
    n,m = map(int,input().split())
    a = [0 for i in range(m)]
    b = [0 for i in range(m)]
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print(a,b)
