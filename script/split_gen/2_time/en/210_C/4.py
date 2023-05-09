def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    #print(N, K)
    #print(C)
    ans = 0
    for i in range(N - K + 1):
        ans = max(ans, len(set(C[i:i+K])))
    print(ans)
