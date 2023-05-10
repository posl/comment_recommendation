def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    l = []
    for i in range(m-1):
        l.append(x[i+1]-x[i])
    l.sort(reverse=True)
    print(sum(l[n-1:]))
