Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x**2, x))**0.5)
    print(max(map(abs, x)))

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = [abs(i) for i in x]
    print(sum(x))
    print(sum([i**2 for i in x])**0.5)
    print(max(x))

=======
Suggestion 3

def main():
    import sys
    N = int(input())
    x = list(map(int, input().split()))
    if (N != len(x)):
        print("N != len(x)")
        sys.exit()
    if (N < 1 or N > 10**5):
        print("N < 1 or N > 10**5")
        sys.exit()
    for i in range(N):
        if (x[i] < -10**5 or x[i] > 10**5):
            print("x[", i, "] < -10**5 or x[", i, "] > 10**5", sep="")
            sys.exit()
    print(sum(abs(x[i]) for i in range(N)))
    print(sum(x[i]**2 for i in range(N))**(1/2))
    print(max(abs(x[i]) for i in range(N)))

=======
Suggestion 4

def manhattan(x):
    return sum([abs(i) for i in x])

=======
Suggestion 5

def cal_manhattan_distance(dimension, point_list):
    distance = 0
    for point in point_list:
        distance += abs(point)
    return distance

=======
Suggestion 6

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 7

def manhattan_distance(x):
    return sum(map(abs, x))

=======
Suggestion 8

def ManhattanDistance(x):
    return sum(map(abs, x))
