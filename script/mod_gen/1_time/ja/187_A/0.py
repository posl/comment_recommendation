def main():
    A, B = map(int, input().split())
    S_A = sum(map(int, list(str(A))))
    S_B = sum(map(int, list(str(B))))
    print(max(S_A, S_B))
main()
