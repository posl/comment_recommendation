Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # A, B = map(int, input().split())
    A, B = 6, 4
    print(32 ** (A - B))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(32 ** (a - b))

=======
Suggestion 3

def solve():
    A, B = map(int, input().split())
    ans = 1
    for i in range(A - B):
        ans *= 32
    print(ans)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    print(32**(a-b))
main()

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(32 ** (A - B))
