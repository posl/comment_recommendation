def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    l = [k//n]*n
    for i in range(k%n):
        l[i] += 1
    for i in range(n):
        print(l[a.index(a[i])])
