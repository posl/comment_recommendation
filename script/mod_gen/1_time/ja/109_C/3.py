def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    x_diff = [x[i+1] - x[i] for i in range(N)]
    #print(x_diff)
    #print("N:", N)
    #print("X:", X)
    #print("x:", x)
    #print("x_diff:", x_diff)
    if N == 1:
        print(x_diff[0])
    else:
        D = x_diff[0]
        for i in range(1, N):
            D = gcd(D, x_diff[i])
        print(D)

if __name__ == '__main__':
    main()