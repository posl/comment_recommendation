def read_input():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    return N, K, H

if __name__ == '__main__':
    read_input()