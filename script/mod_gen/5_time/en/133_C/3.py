def main():
    L, R = map(int, input().split())
    if R - L >= 2019:
        print(0)
    else:
        min = 2019
        for i in range(L, R):
            for j in range(i+1, R+1):
                if min > (i*j)%2019:
                    min = (i*j)%2019
        print(min)

if __name__ == '__main__':
    main()