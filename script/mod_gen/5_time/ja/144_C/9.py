def main():
    N = int(input())
    i = 1
    j = 1
    count = 0
    while True:
        if N <= i*j:
            break
        if i == j:
            j += 1
            count += 1
        else:
            i += 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()