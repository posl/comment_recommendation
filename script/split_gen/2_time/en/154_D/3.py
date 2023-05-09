def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            ans = sum([x+1 for x in p[:K]])/K
        else:
            ans = max(ans, sum([x+1 for x in p[i:i+K]])/K)
    print(ans)
