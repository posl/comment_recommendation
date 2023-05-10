def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            exit()

if __name__ == '__main__':
    main()