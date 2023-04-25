Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N // 2] - d[N // 2 - 1])

=======
Suggestion 2

def main():
    N = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    print(d[N//2] - d[N//2-1])

=======
Suggestion 3

def main():
    # input
    N = int(input())
    ds = [*map(int, input().split())]

    # compute
    ds.sort()
    K = ds[N//2]

    # output
    print(K-ds[N//2-1])

=======
Suggestion 4

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort(reverse = True)
    print(d[N//2] - d[N//2 - 1])

=======
Suggestion 5

def main():
    n = int(input())
    d = list(map(int, input().split()))

    d.sort()
    print(d[n//2] - d[n//2-1])

=======
Suggestion 6

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    k = d[N//2]
    print(k - d[N//2 - 1])

=======
Suggestion 7

def main():
    #input
    N = int(input())
    d = list(map(int, input().split()))

    #count
    d.sort()
    print(d[N//2] - d[N//2-1])
