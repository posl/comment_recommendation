def main():
    n, x = map(int, input().split())
    xlist = list(map(int, input().split()))
    xlist.append(x)
    xlist.sort()
    xlist = [xlist[i+1]-xlist[i] for i in range(n)]
    print(gcd_list(xlist))
