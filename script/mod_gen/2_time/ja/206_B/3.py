def main():
    n = int(input())
    i = 1
    sum = 0
    while sum < n:
        sum += i
        i += 1
    print(i-1)

if __name__ == '__main__':
    main()