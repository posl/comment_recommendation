def main():
    n = int(input())
    sum = 0
    for i in range(1, n):
        sum += i
        if sum >= n:
            print(sum - n + i)
            break

if __name__ == '__main__':
    main()