def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = []
    for i in range(K, N):
        if P[i] > max(P[i - K:i]):
            ans.append('Yes')
        else:
            ans.append('No')
    print('
'.join(ans))
