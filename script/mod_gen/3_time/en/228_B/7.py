def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    X -= 1
    B = [0]*N
    B[X] = 1
    while True:
        X = A[X]
        if B[X]:
            print(-1)
            return
        B[X] = 1
        if X == 1:
            break
    print(sum(B))
main()

if __name__ == '__main__':
    main()