def main():
    L,R = map(int,input().split())
    if L+2019<=R:
        print(0)
    else:
        min_ = 2019
        for i in range(L,R+1):
            for j in range(i+1,R+1):
                if min_>i*j%2019:
                    min_ = i*j%2019
        print(min_)

if __name__ == '__main__':
    main()