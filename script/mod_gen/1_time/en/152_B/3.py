def main():
    a, b = [int(x) for x in input().split()]
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

if __name__ == '__main__':
    main()