def main():
    n = int(input())
    sum = 0
    for i in range(1, 100000):
        sum += i
        if sum >= n:
            print(i)
            break

if __name__ == '__main__':
    main()