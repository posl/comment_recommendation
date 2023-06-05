def main():
    a = input()
    b = a.split()
    c = []
    for i in b:
        c.append(chr(int(i)+96))
    print(''.join(c))

if __name__ == '__main__':
    main()