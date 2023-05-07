def main():
    A, B, X = map(int, input().split())
    N = 0
    if A * N + B * len(str(N)) <= X:
        N = X // A
        while A * N + B * len(str(N)) > X:
            N -= 1
    print(N)
main()

if __name__ == '__main__':
    main()