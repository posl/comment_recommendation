def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(max(a)) + 1)

if __name__ == '__main__':
    main()