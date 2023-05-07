def main():
    a, b = [int(x) for x in input().split()]
    print(max(a+b, a-b, a*b))

if __name__ == '__main__':
    main()