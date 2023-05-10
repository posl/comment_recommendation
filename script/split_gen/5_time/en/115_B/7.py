def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(int(sum(p) - p[N - 1] / 2))
