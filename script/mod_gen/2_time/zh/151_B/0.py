def get_input():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, M, A

if __name__ == '__main__':
    get_input()