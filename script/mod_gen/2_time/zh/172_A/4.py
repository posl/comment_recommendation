def main():
    a = int(input())
    sum = 0
    for i in range(1,4):
        sum += a**i
    print(sum)

if __name__ == '__main__':
    main()