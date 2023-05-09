def get_input():
    # read input from stdin
    N = int(input())
    S = [list(input()) for _ in range(N)]
    T = [list(input()) for _ in range(N)]
    return N, S, T

if __name__ == '__main__':
    get_input()