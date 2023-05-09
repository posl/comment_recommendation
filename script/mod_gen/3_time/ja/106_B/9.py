def main():
    n = int(input())
    count = 0
    for i in range(1, n+1, 2):
        if is_prime(i):
            continue
        if count_divisor(i) == 8:
            count += 1
    print(count)

if __name__ == '__main__':
    main()