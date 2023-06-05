def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        X, Y = map(int, input().split())
        x.append(X)
        y.append(Y)
    print(len(set(zip(x, y))))

if __name__ == '__main__':
    main()