def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    X = A[X]
    count = 0
    while X != 1:
        X = A[X]
        count += 1
        if count > 100:
            break
    if count > 100:
        print(-1)
    else:
        print(count+1)

if __name__ == '__main__':
    main()