def main():
    A, B, T = map(int, input().split())
    print(sum([B for i in range(1, T//A + 2) if A*i <= T + 0.5]))
