def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if l > 0:
        if r > 0:
            print(sum(a) - (a[0] + a[1] - l - r) * 2)
        else:
            print(sum(a) - (a[0] - l) * 2)
    else:
        if r > 0:
            print(sum(a) - (a[1] - r) * 2)
        else:
            print(sum(a))
