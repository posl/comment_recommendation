def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()