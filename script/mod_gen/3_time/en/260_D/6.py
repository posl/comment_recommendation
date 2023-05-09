def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # 1-indexed
    cards = [0] + P
    # 1-indexed
    eaten = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> move number
    move = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    next_card = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    prev_card = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    next_eaten = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    prev_eaten = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    next_larger = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    prev_larger = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    next_smaller = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    prev_smaller = [0] * (N + 1)
    # 1-indexed
    # 1-indexed
    # card number -> card number
    # card number -> card number
    next_smaller_or_equal = [0] * (N + 1

if __name__ == '__main__':
    main()