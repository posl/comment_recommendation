def main():
    N = int(input())
    h = list(map(int,input().split()))
    l = 0
    r = 0
    count = 0
    for i in range(N):
        if h[i] > 0:
            l = i
            break
    for i in range(N-1,-1,-1):
        if h[i] > 0:
            r = i
            break
    #print(l,r)
    while l <= r:
        while l <= r and h[l] > 0:
            h[l] -= 1
            count += 1
            l += 1
        while l <= r and h[r] > 0:
            h[r] -= 1
            count += 1
            r -= 1
    print(count)
main()
