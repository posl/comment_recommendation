def main():
    N = int(input())
    x = list(map(int,input().split()))
    manhattan = 0
    euclidean = 0
    chebyshev = 0
    for i in range(N):
        manhattan += abs(x[i])
        euclidean += abs(x[i])**2
        if chebyshev < abs(x[i]):
            chebyshev = abs(x[i])
    print(manhattan)
    print(euclidean**(1/2))
    print(chebyshev)

if __name__ == '__main__':
    main()