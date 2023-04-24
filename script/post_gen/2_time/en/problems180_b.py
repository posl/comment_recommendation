Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i**2 for i in x]))**(1/2))
    print(max([abs(i) for i in x]))

=======
Suggestion 2

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x ** 2, x)) ** 0.5)
    print(max(map(abs, x)))

=======
Suggestion 3

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x_i) for x_i in x]))
    print((sum([x_i**2 for x_i in x]))**(1/2))
    print(max([abs(x_i) for x_i in x]))

=======
Suggestion 4

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print((sum(map(lambda i: i*i, x)))**(1/2))
    print(max(map(abs, x)))

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(abs(i) for i in x))
    print((sum(i**2 for i in x))**0.5)
    print(max(abs(i) for i in x))

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    for i in range(3):
        if i == 0:
            ans = sum([abs(x[j]) for j in range(n)])
        elif i == 1:
            ans = sum([x[j]**2 for j in range(n)])**(1/2)
        elif i == 2:
            ans = max([abs(x[j]) for j in range(n)])
        print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def manhattan_dist(x):
    return sum(abs(x_i) for x_i in x)

=======
Suggestion 9

def manhattan_distance(A):
    return sum(abs(a) for a in A)
