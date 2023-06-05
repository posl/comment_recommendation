def main():
    n = int(input().split()[0])
    p = list(map(int, input().split()))
    x = int(input().split()[1])
    print(p.index(x)+1)

if __name__ == '__main__':
    main()