def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    print(abs(p.index(1)-q.index(1)))

if __name__ == '__main__':
    main()