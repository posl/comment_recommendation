def get_layers(N,X):
    if N == 0:
        return 1
    elif X <= 1:
        return 0
    elif X <= 1 + 2 ** (N-1):
        return get_layers(N-1,X-1)
    elif X == 1 + 2 ** (N-1) + 1:
        return 2 ** N - 1
    elif X <= 2 * (1 + 2 ** (N-1)):
        return 2 ** N - 1 + get_layers(N-1,X-1-2**(N-1)-1)
    elif X == 2 * (1 + 2 ** (N-1)) + 1:
        return 2 ** (N+1) - 1
N,X = map(int,input().split())
print(get_layers(N,X))

if __name__ == '__main__':
    get_layers()