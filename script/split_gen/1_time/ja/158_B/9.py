def main():
    N, A, B = map(int, input().split())
    print(min(N, A) - abs(A - B) // 2)
