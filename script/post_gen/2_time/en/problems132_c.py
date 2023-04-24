Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2] - d[N//2 - 1])

=======
Suggestion 2

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2] - d[n//2-1])

=======
Suggestion 3

def main():
    #input
    N = int(input())
    ds = input().split()
    for i in range(N):
        ds[i] = int(ds[i])
    #sort
    ds = sorted(ds)
    #output
    print(ds[N//2]-ds[N//2-1])
