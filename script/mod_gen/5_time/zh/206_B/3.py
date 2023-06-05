def main():
    N = int(input())
    i = 1
    sum = 0
    while True:
        sum += i
        if sum >= N:
            break
        i += 1
    print(i)

if __name__ == '__main__':
    main()