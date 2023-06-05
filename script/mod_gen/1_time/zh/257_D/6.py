def main():
    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        x1, y1, P1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        P.append(P1)
    print(N)

if __name__ == '__main__':
    main()