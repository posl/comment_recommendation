def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if not "7" in str(i) and not "7" in str(oct(i)):
            count += 1
    print(count)

if __name__ == '__main__':
    main()