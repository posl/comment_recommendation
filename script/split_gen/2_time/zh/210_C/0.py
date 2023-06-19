def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    s = set()
    for i in range(N-K+1):
        s.add(len(set(C[i:i+K])))
    print(max(s))
