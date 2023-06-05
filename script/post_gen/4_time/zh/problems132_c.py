Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()
    K = D[N//2]
    print(D[N//2] - D[N//2-1])

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if N % 2 == 0:
        print(d[N//2] - d[N//2-1])
    else:
        print(0)

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2] - d[n//2 - 1])

=======
Suggestion 4

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    mid = N//2
    if d[mid] == d[mid-1]:
        print(0)
    else:
        print(d[mid]-d[mid-1])

=======
Suggestion 5

def main():
    n = int(input())
    d = list(map(int,input().split()))
    d = sorted(d)
    if n%2 == 0:
        print(d[n//2]-d[n//2-1])
    else:
        print(0)

=======
Suggestion 6

def solve(N, D):
    D.sort()
    mid = N // 2
    return D[mid] - D[mid-1]

=======
Suggestion 7

def main():
    n=int(input())
    d=[int(i) for i in input().split()]
    d.sort()
    count=0
    for i in range(n//2,n):
        if d[i]>d[i-1]:
            count+=1
    print(count)

=======
Suggestion 8

def solve():
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()
    print(D[N//2]-D[N//2-1])
solve()

=======
Suggestion 9

def problems132_c():
    pass

=======
Suggestion 10

def main():
    n = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    print(d[n//2]-d[n//2-1])
