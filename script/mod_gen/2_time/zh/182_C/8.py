def main():
    n = int(input())
    if n % 3 == 0:
        print(0)
        return
    digit_sum = 0
    for c in str(n):
        digit_sum += int(c)
    if digit_sum % 3 == 0:
        print(1)
        return
    if n >= 100 and n % 3 == 1:
        print(2)
        return
    if n >= 10 and n % 3 == 2:
        print(2)
        return
    print(-1)

if __name__ == '__main__':
    main()