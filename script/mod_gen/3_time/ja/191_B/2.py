def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i for i in A if i != X]
    print(*A)

if __name__ == '__main__':
    main()