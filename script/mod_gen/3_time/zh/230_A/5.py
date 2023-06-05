def main():
    n = int(input())
    if n >= 1 and n <= 9:
        print('AGC00' + str(n))
    elif n >= 10 and n <= 99:
        print('AGC0' + str(n))
    elif n >= 100 and n <= 999:
        print('AGC' + str(n))

if __name__ == '__main__':
    main()