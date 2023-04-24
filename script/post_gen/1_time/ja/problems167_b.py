Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 2

def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A+B:
        print(A)
    else:
        print(A-(K-(A+B)))
