Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2]-d[N//2-1])

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2] - d[N//2 -1])

main()

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int,input().split()))
    d.sort()
    print(d[n//2] - d[n//2-1])

=======
Suggestion 4

def main():
    n = int(input())
    ds = [int(x) for x in input().split()]
    ds.sort()
    print(ds[n//2] - ds[n//2-1])
