def main():
    n,m = map(int,input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(n):
        print(a.count(i+1) + b.count(i+1))
