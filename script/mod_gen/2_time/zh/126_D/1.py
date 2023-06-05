def main():
    n,k = map(int,input().split())
    p = 0
    for i in range(1,n+1):
        if i >= k:
            p += 1/n
        elif i < k:
            x = i
            while x < k:
                x *= 2
            p += 1/n * (0.5 ** (x/i))
    print(p)

if __name__ == '__main__':
    main()