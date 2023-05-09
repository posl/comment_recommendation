def main():
    A, B, C = map(int, input().rstrip().split())
    print(max(C - (A - B), 0))
