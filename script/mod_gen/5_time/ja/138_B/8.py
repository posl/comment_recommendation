def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(list(map(lambda x: 1 / x, a))))

if __name__ == '__main__':
    main()