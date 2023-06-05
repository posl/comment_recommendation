def get_input():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    return N, K, LRs

if __name__ == '__main__':
    get_input()