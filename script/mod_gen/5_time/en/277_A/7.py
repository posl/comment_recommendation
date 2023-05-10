def main():
    n = int(input())
    x = int(input())
    p = [int(i) for i in input().split()]
    print(p.index(x)+1)

if __name__ == '__main__':
    main()