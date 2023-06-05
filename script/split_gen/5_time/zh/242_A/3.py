def main():
    A, B, C, X = map(int, input().split())
    print(C/(B-A) if A <= X <= B else 0)
