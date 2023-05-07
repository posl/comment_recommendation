def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [i for i in a if i != x]
    print(*b)

if __name__ == '__main__':
    main()