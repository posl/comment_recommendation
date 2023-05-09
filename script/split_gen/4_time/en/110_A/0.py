def main():
    A, B, C = map(int, input().split())
    print(A + B + C + max(A * 10 + B + C, A + B * 10 + C, A + B + C * 10))
