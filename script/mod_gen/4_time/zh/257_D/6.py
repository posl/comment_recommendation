def main():
    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    print(N)
    print(x)
    print(y)
    print(P)

if __name__ == '__main__':
    main()