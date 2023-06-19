def main():
    n, x = map(int, input().split())
    xlist = list(map(int, input().split()))
    xlist.append(x)
    xlist.sort()
    diff = [xlist[i+1]-xlist[i] for i in range(n)]
    d = diff[0]
    for i in range(1, n):
        d = gcd(d, diff[i])
    print(d)
