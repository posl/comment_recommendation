def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    X = A[X]
    count = 1
    while A[X] != X:
        X = A[X]
        count += 1
    print(count)

if __name__ == '__main__':
    main()