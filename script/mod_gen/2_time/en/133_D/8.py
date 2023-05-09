def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2x liters of rain = x liters of water
    # A_i = x + x + x + x
    # A_i = 4x
    # x = A_i / 4
    # 2x liters of rain = x liters of water
    # 2x = A_i / 4
    # x = A_i / 8
    # A_i = 8x
    # A_i = 8(A_i / 8) = 8(A_i // 8)
    # A_i = 8(A_i // 8) + (A_i % 8)

if __name__ == '__main__':
    main()