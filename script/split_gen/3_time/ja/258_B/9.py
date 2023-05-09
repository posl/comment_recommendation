def main():
    N = int(input())
    A = [list(map(int, list(input()))) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            # 0 0 0 0 0
            # 0 1 1 1 0
            # 0 1 0 1 0
            # 0 1 1 1 0
            # 0 0 0 0 0
            # というマス目の場合、
            # 0 0 0
