def main():
    A, B = map(int, input().split())
    print(B - A + 1 if A <= B else 0)
