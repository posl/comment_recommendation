def main():
    n,k = map(int,input().split())
    if n >= k:
        print(1)
        return
    p = 1
    for i in range(1,n):
        if i >= k:
            break
        t = 1
        while i*t < k:
            t *= 2
        p += 1/(n*t)
    print(p/2)
main()
