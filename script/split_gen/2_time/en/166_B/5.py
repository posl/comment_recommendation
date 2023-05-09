def main():
    N, K = map(int, input().split())
    S = set()
    for _ in range(K):
        d = int(input())
        for a in map(int, input().split()):
            S.add(a)
    print(N - len(S))
