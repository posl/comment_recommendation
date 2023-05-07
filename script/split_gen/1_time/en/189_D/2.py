def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if S[-1] == 'AND':
        print(2 ** (N + 1) - 2 ** N)
    else:
        print(2 ** (N + 1))
