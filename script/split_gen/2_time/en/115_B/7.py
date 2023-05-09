def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p = sorted(p, reverse=True)
    for i in range(1, N):
        p[0] = int(p[0] / 2)
    print(sum(p))
