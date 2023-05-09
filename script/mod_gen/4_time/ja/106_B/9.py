def main():
    N = int(input())
    count = 0
    for i in range(1,N+1,2):
        if i % 2 == 0:
            continue
        divisor = 0
        for j in range(1,i+1):
            if i % j == 0:
                divisor += 1
        if divisor == 8:
            count += 1
    print(count)

if __name__ == '__main__':
    main()