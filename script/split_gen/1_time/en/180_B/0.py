def main():
    N = int(input())
    x = [int(i) for i in input().split()]
    manhattan = 0
    euclidian = 0
    chebyshev = 0
    for i in range(N):
        manhattan += abs(x[i])
        euclidian += abs(x[i]) ** 2
        if chebyshev < abs(x[i]):
            chebyshev = abs(x[i])
    euclidian = euclidian ** (1/2)
    print(manhattan)
    print(euclidian)
    print(chebyshev)
