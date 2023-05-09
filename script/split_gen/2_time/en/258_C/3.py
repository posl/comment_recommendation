def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    print(N, Q)
    print(S)
    print(queries)
