def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i % 2 == 1:
            X -= A[i] - 1
        else:
            X -= A[i]
    if X >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()