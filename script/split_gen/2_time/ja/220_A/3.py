def main():
    # A, B, C = map(int, input().split())
    A, B, C = 123, 456, 100
    # A, B, C = 630, 940, 314
    # A, B, C = 1, 1000, 1
    # A, B, C = 1, 1000, 1000
    if A > B:
        print(-1)
        return
    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            return
    print(-1)
