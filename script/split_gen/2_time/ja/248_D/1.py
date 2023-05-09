def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        l,r,x = map(int,input().split())
        print(a[l-1:r].count(x))
