def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(n+1)
    l = []
    for i in range(k):
        l.append(a[i+1]-a[i]-1)
    l.append(a[0]-1)
    print(n-max(l))
