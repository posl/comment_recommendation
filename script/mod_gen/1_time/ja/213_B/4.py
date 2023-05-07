def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sorted(A)[1])

if __name__ == '__main__':
    main()