def main():
    A, B, C = map(int, input().split())
    print(C if A >= B + C else B + C - A)
