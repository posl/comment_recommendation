def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    l = 0
    r = n
    while l + 1 < r:
        mid = (l + r) // 2
        #print(l, r, mid)
        if check(mid, n, s, w):
            l = mid
        else:
            r = mid
    print(l)
