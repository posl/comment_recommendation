def main():
    N, M = map(int, input().split())
    ab = []
    for i in range(M):
        a, b = map(int, input().split())
        ab.append((a, b))
    print(ab)
    print(N, M)
