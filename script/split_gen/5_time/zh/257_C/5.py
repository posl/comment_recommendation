def main():
    n = int(input())
    s = input()
    w = [int(i) for i in input().split()]
    l,r = 0,10**9
    while l+1<r:
        mid = (l+r)//2
        cnt = 0
        for i in range(n):
            if s[i]=='0' and w[i]<=mid:
                cnt += 1
            if s[i]=='1' and w[i]>mid:
                cnt += 1
        if cnt==n:
            l = mid
        else:
            r = mid
    print(l)
