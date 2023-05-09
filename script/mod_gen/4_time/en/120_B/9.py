def main():
    a,b,k = map(int,input().split())
    count = 0
    for i in range(1,100):
        if a%i==0 and b%i==0:
            count += 1
            if count == k:
                print(i)
                return

if __name__ == '__main__':
    main()