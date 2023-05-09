def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(sorted(a)[1]) + 1)

if __name__ == '__main__':
    main()