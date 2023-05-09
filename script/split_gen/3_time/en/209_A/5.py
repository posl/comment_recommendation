def main():
    A, B = map(int, input().split())
    print(max(B - A + 1, 0))
