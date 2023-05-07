def main():
    l,r = map(int,input().split())
    if (r-l) >= 2019:
        print(0)
        exit()
    else:
        m = 2019
        for i in range(l,r):
            for j in range(i+1,r+1):
                x = (i*j)%2019
                if x < m:
                    m = x
                    if m == 0:
                        print(m)
                        exit()
        print(m)
        exit()

if __name__ == '__main__':
    main()