def main():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(a[0]*b[1]-a[1]*b[0])

if __name__ == '__main__':
    main()