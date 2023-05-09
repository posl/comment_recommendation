def main():
    n = int(input())
    sum = 0
    i = 0
    while sum < n:
        i += 1
        sum += i
    print(i)

if __name__ == '__main__':
    main()