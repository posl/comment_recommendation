def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 0
    for i in range(N):
        if X == A[X]:
            print(count)
            break
        else:
            X = A[X]
            count += 1
    else:
        print(-1)

if __name__ == '__main__':
    main()