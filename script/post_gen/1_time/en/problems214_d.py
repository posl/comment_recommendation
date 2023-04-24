Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    u = [0] * (N - 1)
    v = [0] * (N - 1)
    w = [0] * (N - 1)
    for i in range(N - 1):
        u[i], v[i], w[i] = map(int, input().split())
