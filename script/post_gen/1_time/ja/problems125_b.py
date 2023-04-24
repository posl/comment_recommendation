Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    V = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    V = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)
