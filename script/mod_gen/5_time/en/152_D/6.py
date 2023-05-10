def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i % 10 == 0:
            continue
        else:
            first_digit = int(str(i)[0])
            last_digit = int(str(i)[-1])
            if first_digit == last_digit:
                count += 1
    print(count * count)

if __name__ == '__main__':
    main()