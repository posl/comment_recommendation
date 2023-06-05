def main():
    n,q = map(int,input().split())
    s = input()
    a = [0]*(n+1)
    for i in range(n):
        if s[i:i+2] == "AC":
            a[i+1] = a[i] + 1
        else:
            a[i+1] = a[i]
    for _ in range(q):
        l,r = map(int,input().split())
        print(a[r-1]-a[l-1])
