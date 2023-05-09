def main():
    N = int(input())
    f = [0] * N
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        f[u - 1] += w
        f[v - 1] += w
    print(sum(f) // 2)
