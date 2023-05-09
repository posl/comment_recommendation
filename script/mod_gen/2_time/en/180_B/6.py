def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    x = list(map(int, input().split()))
    #print(N, x)
    manhattan = 0
    euclidian = 0
    chebyshev = 0
    for i in range(N):
        manhattan += abs(x[i])
        euclidian += abs(x[i])**2
        if chebyshev < abs(x[i]):
            chebyshev = abs(x[i])
    euclidian = euclidian**(1/2)
    print(manhattan)
    print(euclidian)
    print(chebyshev)

if __name__ == '__main__':
    main()