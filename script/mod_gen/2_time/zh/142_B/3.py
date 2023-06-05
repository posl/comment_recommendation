def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i%2 != 0:
            count += 1
    print(count/n)

if __name__ == '__main__':
    main()