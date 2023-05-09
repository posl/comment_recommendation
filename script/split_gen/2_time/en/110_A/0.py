def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, 10 * A + B + C, A + 10 * B + C, A + B + 10 * C, 10 * A + 10 * B + C, 10 * A + B + 10 * C, A + 10 * B + 10 * C, 10 * A + 10 * B + 10 * C))
