def main():
    import sys
    import math
    def solve(A: int, B: int):
        x = B / math.sqrt(A * A + B * B)
        y = A / math.sqrt(A * A + B * B)
        return x, y
    A, B = map(int, input().split())
    ans = solve(A, B)
    print(ans[0], ans[1])

if __name__ == '__main__':
    main()