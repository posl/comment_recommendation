def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 0
    for i in range(1, N+1):
        if i == X:
            break
        else:
            count += 1
            X = A[X]
    print(count)

if __name__ == '__main__':
    main()