def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(*[i for i in A if i != X])

if __name__ == '__main__':
    main()