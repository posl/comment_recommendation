def main():
    N, K = map(int, input().split())
    S = [0] * N
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for a in A:
            S[a-1] += 1
    print(S.count(0))
