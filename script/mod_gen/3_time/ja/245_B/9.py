def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(min(set(range(2001)) - set(A)))

if __name__ == '__main__':
    main()