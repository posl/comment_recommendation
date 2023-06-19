def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min = 0
    if n % a != 0:
        min += 1
    min += int(n / a)
    if n % b != 0:
        min += 1
    min += int(n / b)
    if n % c != 0:
        min += 1
    min += int(n / c)
    if n % d != 0:
        min += 1
    min += int(n / d)
    if n % e != 0:
        min += 1
    min += int(n / e)
    print(min)
    return 0

if __name__ == '__main__':
    main()