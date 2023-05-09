def get_input():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    return N, M, edges

if __name__ == '__main__':
    get_input()