Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems105_a():
    n,k = map(int,input().split())
    if n%k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    print(N%K)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    print(N-K if K>1 else 0)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    print(0 if n%k==0 else 1)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(0 if N % K == 0 else 1)

=======
Suggestion 6

def get_input():
    line = raw_input()
    line = line.split(' ')
    n = int(line[0])
    k = int(line[1])
    return n, k
