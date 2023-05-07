def main():
    N = int(input())
    X = [0 for i in range(N)]
    Y = [0 for i in range(N)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    print(N)
main()

if __name__ == '__main__':
    main()