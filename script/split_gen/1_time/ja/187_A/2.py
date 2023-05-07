def main():
    A, B = map(int, input().split())
    S_A = sum(map(int, str(A)))
    S_B = sum(map(int, str(B)))
    print(max(S_A, S_B))
