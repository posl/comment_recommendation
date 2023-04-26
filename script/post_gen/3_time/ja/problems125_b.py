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
        if V[i] - C[i] > 0:
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
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += max(v[i]-c[i], 0)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(sum([V[i]-C[i] if V[i]-C[i]>0 else 0 for i in range(N)]))

=======
Suggestion 7

def main():
    #input
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #compute
    ans = 0
    for i in range(N):
        if V[i]-C[i] > 0:
            ans += V[i]-C[i]
    #output
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # print(n, v, c)
    ans = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            ans += v[i] - c[i]
    print(ans)
