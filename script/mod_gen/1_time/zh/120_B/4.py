def main():
    a,b,k = map(int,input().split())
    array = []
    for i in range(1,101):
        if a % i == 0 and b % i == 0:
            array.append(i)
    print(array[-k])

if __name__ == '__main__':
    main()