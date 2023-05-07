def main():
    l, r = map(int, input().split())
    minmod = 2018
    for i in range(l, r):
        for j in range(i+1, r+1):
            minmod = min(minmod, (i*j)%2019)
    print(minmod)

if __name__ == '__main__':
    main()