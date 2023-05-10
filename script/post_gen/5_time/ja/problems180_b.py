Synthesizing 8/10 solutions

=======
Suggestion 1

def manhattan_distance(x):
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i])
    return sum

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int,input().split()))
    x_abs = list(map(abs,x))
    print(sum(x_abs))
    print(sum([x**2 for x in x_abs])**0.5)
    print(max(x_abs))

=======
Suggestion 3

def distance(p, q):
    return abs(p-q)

=======
Suggestion 4

def ManhattanDistance(n, x):
    d = 0
    for i in range(n):
        d += abs(x[i])
    return d

=======
Suggestion 5

def main():
    N = int(input())
    x = list(map(int,input().split()))
    x_abs = [abs(x_i) for x_i in x]
    print(sum(x_abs))
    print(sum([x_i**2 for x_i in x_abs])**(1/2))
    print(max(x_abs))

=======
Suggestion 6

def manhattan_distance(n, x):
    return sum([abs(i) for i in x])

=======
Suggestion 7

def main():
    N = int(input())
    x = list(map(int,input().split()))
    x = [abs(x[i]) for i in range(N)]
    print(sum(x))
    print(sum([x[i]**2 for i in range(N)])**0.5)
    print(max(x))

=======
Suggestion 8

def main():
    N = int(input())
    x = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    ans3 = 0
    for i in range(N):
        ans1 += abs(x[i])
        ans2 += abs(x[i])**2
        ans3 = max(ans3, abs(x[i]))
    ans2 = ans2**0.5
    print(ans1)
    print(ans2)
    print(ans3)
