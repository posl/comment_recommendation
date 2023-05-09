def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(N - max([A.count(i) for i in set(A)]))

if __name__ == '__main__':
    main()