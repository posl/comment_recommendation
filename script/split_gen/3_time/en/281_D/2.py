def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = {0}
    for i in range(K):
        S = {a+b for a in S for b in A if a+b <= D}
    print(max(S) if max(S) % D == 0 else -1)
