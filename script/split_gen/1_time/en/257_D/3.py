def main():
    n = int(input())
    trampolines = []
    for i in range(n):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    # 2^N
    # 2^20 = 1,048,576
    # 1,048,576 * 10^9 = 10^12
    # 10^12 * 4 = 4 * 10^12
    # 4 * 10^12 = 4,000,000,000,000
    # 4,000,000,000,000 / 10^9 = 4,000,000,000
    # 4,000,000,000 = 4,000,000
    # 4,000,000 = 4,000
    # 4,000 = 4
    # 4 = 2^2
    # 2^2 = 4
    # 2^2 * 10^9 = 4 * 10^9
    # 4 * 10^9 = 4,000,000,000
    # 4,000,000,000 = 4,000,000
    # 4,000,000 = 4,000
    # 4,000 = 4
    # 4 = 2^2
    # 2^2 = 4
    # 2^2 * 10^9 = 4 * 10^9
    # 4 * 10^9 = 4,000,000,000
    # 4,000,000,000 = 4,000,000
    # 4,000,000 = 4,000
    # 4,000 = 4
    # 4 = 2^2
    # 2^2 = 4
    # 2^2 * 10^9 = 4 * 10^9
    # 4 * 10^9 = 4,000,000,000
    # 4,000,000,000 = 4,000,000
    # 4,000,000 = 4,000
    # 4,000 = 4
