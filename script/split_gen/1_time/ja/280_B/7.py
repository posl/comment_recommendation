def main():
    n = int(input())
    s = list(map(int,input().split()))
    a = []
    a.append(s[0])
    for i in range(1,n):
        a.append(s[i]-a[i-1])
    for i in range(n):
        print(a[i],end=' ')
    print()
