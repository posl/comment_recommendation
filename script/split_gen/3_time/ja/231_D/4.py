def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    print("Yes" if solve(N, M, AB) else "No")
