def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print('Yes' if len(set(S)) == N else 'No')
