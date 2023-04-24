Synthesizing 2/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    #print(N, X)
    #print(A)
    #print(B)

    #

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N
