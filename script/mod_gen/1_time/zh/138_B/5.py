def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(lambda x: 1/x, a))
    print(1/sum(b))

if __name__ == '__main__':
    main()