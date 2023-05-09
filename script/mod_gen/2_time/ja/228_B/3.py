def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    X -= 1
    count = 0
    while True:
        X = A[X]
        count += 1
        if X == 1:
            break
        if count == N:
            count = -1
            break
    print(count)

if __name__ == '__main__':
    main()