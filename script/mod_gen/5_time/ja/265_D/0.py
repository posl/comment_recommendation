def get_input():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    return N, P, Q, R, A

if __name__ == '__main__':
    get_input()