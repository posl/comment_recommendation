def main():
    L,R = map(int, input().split())
    min = 2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            tmp = (i*j)%2019
            if tmp < min:
                min = tmp
    print(min)

if __name__ == '__main__':
    main()