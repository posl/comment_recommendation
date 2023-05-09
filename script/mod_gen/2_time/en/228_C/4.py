def get_input():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    return N, K, P

if __name__ == '__main__':
    get_input()