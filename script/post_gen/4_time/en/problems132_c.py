Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2]-d[n//2-1])

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2] - d[N//2-1])

=======
Suggestion 3

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[int(N/2)]-d[int(N/2)-1])

=======
Suggestion 4

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 6
    a = [9, 1, 4, 4, 6, 7]
    #n = 8
    #a = [9, 1, 14, 5, 5, 4, 4, 14]
    #n = 14
    #a = [99592, 10342, 29105, 78532, 83018, 11639, 92015, 77204, 30914, 21912, 34519, 80835, 100000, 1]
    a.sort()
    print(a)
    print(sum(a[0::2]) - sum(a[1::2]))

=======
Suggestion 5

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    d.sort()
    print(d[n//2] - d[n//2-1])

=======
Suggestion 6

def main():
    N = int(input())
    d = [int(x) for x in input().split()]
    d.sort()
    print(d[N//2] - d[N//2 - 1])

=======
Suggestion 7

def solve():
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()
    print(D[N//2] - D[N//2-1])

=======
Suggestion 8

def get_input():
    n = int(input())
    d = list(map(int, input().split()))
    return n, d

=======
Suggestion 9

def problems132_c():
    # Get input
    n = int(input())
    d = list(map(int, input().split()))

    # Sort list
    d.sort()

    # Get median
    median = d[int(n/2)]

    # Get result
    result = d[int(n/2)] - d[int(n/2)-1]

    # Print result
    print(result)
