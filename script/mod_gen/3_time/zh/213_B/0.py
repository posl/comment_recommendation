def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = sorted(a)
    print(a.index(b[1])+1)

if __name__ == '__main__':
    main()