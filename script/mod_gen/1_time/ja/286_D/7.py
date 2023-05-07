def main():
    N, X = map(int, input().split())
    for i in range(N):
        A, B = map(int, input().split())
        X -= A * B
    print("Yes" if X == 0 else "No")

if __name__ == '__main__':
    main()