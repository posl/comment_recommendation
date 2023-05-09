def main():
    n = int(input())
    sum = 0
    i = 1
    while sum < n:
        sum += i
        i += 1
    print(i-1)

if __name__ == '__main__':
    main()