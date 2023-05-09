def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(N * max(a) - sum(a))

if __name__ == '__main__':
    main()