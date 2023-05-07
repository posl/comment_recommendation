def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - N)

if __name__ == '__main__':
    main()