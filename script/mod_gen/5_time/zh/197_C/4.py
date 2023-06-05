def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 2**30
    for i in range(n):
        xor = 0
        or_ = 0
        for j in range(i,n):
            xor ^= a[j]
            or_ |= a[j]
            if ans < xor ^ or_:
                break
            ans = min(ans,xor ^ or_)
    print(ans)

if __name__ == '__main__':
    main()