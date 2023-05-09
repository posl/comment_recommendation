def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(360 - sum(A))

if __name__ == '__main__':
    main()