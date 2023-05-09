def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(K, N):
        ans.append(str(min(P[i-K:i+1])))
    print('
'.join(ans))
