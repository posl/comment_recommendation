def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for i in range(M)]
    L = [LR[i][0] for i in range(M)]
    R = [LR[i][1] for i in range(M)]
    if max(L) > min(R):
        print(0)
    else:
        print(min(R) - max(L) + 1)
