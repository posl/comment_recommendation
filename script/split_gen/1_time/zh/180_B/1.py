def main():
    N = int(input())
    X = list(map(int,input().split()))
    manhattan_distance = 0
    euclidean_distance = 0
    chebyshev_distance = 0
    for i in range(N):
        manhattan_distance += abs(X[i])
        euclidean_distance += X[i]**2
        chebyshev_distance = max(chebyshev_distance,abs(X[i]))
    euclidean_distance = euclidean_distance**0.5
    print(manhattan_distance)
    print(euclidean_distance)
    print(chebyshev_distance)
