def main():
    N = int(input())
    W = [input() for _ in range(N)]
    print('Yes' if len(W) == len(set(W)) and all(W[i][0] == W[i-1][-1] for i in range(1, N)) else 'No')
