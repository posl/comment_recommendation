Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i**2 for i in x]))**0.5)
    print(max([abs(i) for i in x]))

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i**2 for i in x]))**(1/2))
    print(max([abs(i) for i in x]))

=======
Suggestion 3

def main():
    N = int(input())
    x = list(map(int,input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i**2 for i in x]))**0.5)
    print(max([abs(i) for i in x]))

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x_i) for x_i in x]))
    print(sum([abs(x_i)**2 for x_i in x])**0.5)
    print(max([abs(x_i) for x_i in x]))

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    X = list(map(int,input().split()))
    print(sum(map(abs,X)))
    print((sum(map(lambda x:x**2,X)))**0.5)
    print(max(map(abs,X)))

=======
Suggestion 7

def main():
    N = int(input())
    X = list(map(int, input().split()))
    #print("N =", N)
    #print("X =", X)
    # マンハッタン距離
    sum = 0
    for i in range(N):
        sum += abs(X[i])
    print(sum)
    # ユークリッド距離
    sum = 0
    for i in range(N):
        sum += X[i] * X[i]
    print(sum ** 0.5)
    # チェビシェフ距離
    max = 0
    for i in range(N):
        if max < abs(X[i]):
            max = abs(X[i])
    print(max)

=======
Suggestion 8

def manhattan_distance(x):
    return sum(abs(i) for i in x)
