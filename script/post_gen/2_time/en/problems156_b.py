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
    N, K = map(int, input().split())
    if N == 0:
        print(1)
    else:
        print(len(str(N).replace('0', '')))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(len(str(N // K)))

=======
Suggestion 5

def main():
    N, K = map(int, raw_input().split())
    print len(str(N).encode("hex").decod

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(len(str(N)))
    print(len(str(N)) // K)
