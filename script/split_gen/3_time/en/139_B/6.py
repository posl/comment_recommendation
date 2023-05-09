def main():
    A, B = map(int, input().split())
    if B <= A:
        print(1)
    else:
        print((B - 1) // (A - 1))
