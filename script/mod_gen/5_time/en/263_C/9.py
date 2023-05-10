def solution():
    N, M = map(int, input().split())
    def dfs(arr):
        if len(arr) == N:
            print(" ".join(map(str, arr)))
            return
        for i in range(1, M + 1):
            if arr[-1] < i:
                dfs(arr + [i])
    for i in range(1, M + 1):
        dfs([i])
solution()

if __name__ == '__main__':
    solution()