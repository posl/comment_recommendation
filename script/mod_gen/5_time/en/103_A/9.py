def main():
    a = input()
    b = a.split()
    b = list(map(int, b))
    b.sort()
    print(b[2] - b[0])

if __name__ == '__main__':
    main()