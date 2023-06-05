def main():
    k = int(input())
    count = 0
    for i in range(1,k+1):
        if i % 2 == 0:
            count += (k//2)
        else:
            count += (k//2 + 1)
    print(count)

if __name__ == '__main__':
    main()