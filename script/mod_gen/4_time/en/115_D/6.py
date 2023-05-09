def count_patty(N, X):
    if N == 0:
        return 0
    elif X == 1:
        return 0
    elif X <= 1 + (2**N - 1):
        return count_patty(N-1, X-1)
    elif X == 2 + (2**N - 1):
        return 1 + (2**(N-1))
    elif X <= 2 + 2*(2**N - 1):
        return 1 + (2**(N-1)) + count_patty(N-1, X-2-(2**(N-1)))
    else:
        return 1 + 2*(2**(N-1))
N, X = map(int, input().split())
print(count_patty(N, X))

if __name__ == '__main__':
    count_patty()