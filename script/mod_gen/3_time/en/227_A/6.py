def get_last_card(N, K, A):
    if N == 1:
        return 1
    if K < N:
        return (A + K - 1) % N + 1
    else:
        return (A + K - 1) % N

if __name__ == '__main__':
    get_last_card()