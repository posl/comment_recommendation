def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [x/2 for x in p]
    s = sum(p[:K])
    max_s = s
    for i in range(N-K):
        s = s - p[i] + p[i+K]
        max_s = max(max_s, s)
    print(max_s)
