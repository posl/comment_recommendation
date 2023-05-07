def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]
    N = 5
    ans = 0
    ans = max(A, B, C, D, E)
    ans = ans + (ans - 1) // 9 * 10
    print(ans)
