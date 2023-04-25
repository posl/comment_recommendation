Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    print(len(str(N)))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    print(len(str(N), K))

=======
Suggestion 3

def main():
    import math
    N, K = map(int, input().split())
    print(math.ceil(math.log(N, K)))

=======
Suggestion 4

def main():
    N, K = list(map(int, input().split()))
    print(len(str(N)))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(len(str(N).encode('utf-8')) * 8 // int(math.log2(K)))

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    print(len(str(N).encode('utf-8')))
