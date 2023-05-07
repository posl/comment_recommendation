def get_input():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    return N, intervals

if __name__ == '__main__':
    get_input()