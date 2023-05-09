def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 1
    while True:
        if A[X-1] == X:
            break
        else:
            X = A[X-1]
            count += 1
    print(count)

if __name__ == '__main__':
    main()