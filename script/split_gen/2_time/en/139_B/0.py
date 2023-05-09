def main():
    A, B = map(int, input().split())
    if B == 1:
        print(0)
    else:
        print((B - 2) // (A - 1) + 1)
