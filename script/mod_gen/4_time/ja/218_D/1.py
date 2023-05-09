def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    a = x[0]
    b = x[N-1]
    c = y[0]
    d = y[N-1]
    print((b-a)*(d-c))

if __name__ == '__main__':
    main()