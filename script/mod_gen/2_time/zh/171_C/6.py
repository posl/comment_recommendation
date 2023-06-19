def main():
    n = int(input())
    list = []
    while n > 0:
        m = n % 26
        if m != 0:
            list.append(chr(m + 96))
        else:
            list.append('z')
        n = n // 26
    list.reverse()
    print(''.join(list))

if __name__ == '__main__':
    main()