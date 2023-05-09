def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N or any(W[i][0] != W[i-1][-1] for i in range(1, N)):
        print('No')
    else:
        print('Yes')
