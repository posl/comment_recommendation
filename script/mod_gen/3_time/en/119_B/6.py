def main():
    #input
    N = int(input())
    xus = [input().split() for _ in range(N)]
    #compute
    ans = 0
    for xu in xus:
        x, u = xu
        x = float(x)
        if u == 'JPY':
            ans += x
        else:
            ans += x * 380000.0
    #output
    print(ans)

if __name__ == '__main__':
    main()