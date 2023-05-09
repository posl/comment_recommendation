def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    return N, Q, A, X

if __name__ == '__main__':
    get_input()