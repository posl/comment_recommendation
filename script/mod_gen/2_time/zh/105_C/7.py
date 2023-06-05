def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    s = []
    while n != 0:
        if n % 2 == 0:
            s.append(0)
            n = n // (-2)
        else:
            s.append(1)
            n = (n - 1) // (-2)
    s.reverse()
    print(''.join(map(str, s)))

if __name__ == '__main__':
    main()