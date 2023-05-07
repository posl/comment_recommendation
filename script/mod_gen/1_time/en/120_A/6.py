def main():
    a, b, c = [int(i) for i in input().split()]
    print(min(b // a, c))

if __name__ == '__main__':
    main()