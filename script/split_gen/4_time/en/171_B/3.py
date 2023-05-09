def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = sum(p[:K])
    print(ans)
