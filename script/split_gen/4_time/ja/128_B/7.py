def main():
    # N = int(input())
    # S_P = [input().split() for i in range(N)]
    # S_P = sorted(S_P, key=lambda x: x[1], reverse=True)
    # S_P = sorted(S_P, key=lambda x: x[0])
    # for i in range(N):
    #     print(S_P[i][2])
    # N = int(input())
    # S_P = [input().split() for i in range(N)]
    # S_P = sorted(S_P, key=lambda x: x[0])
    # S_P = sorted(S_P, key=lambda x: x[1], reverse=True)
    # for i in range(N):
    #     print(S_P[i][2])
    N = int(input())
    S_P = [input().split() for i in range(N)]
    S_P = sorted(S_P, key=lambda x: x[0])
    S_P = sorted(S_P, key=lambda x: x[1], reverse=True)
    for i in range(N):
        print(S_P[i][2])
