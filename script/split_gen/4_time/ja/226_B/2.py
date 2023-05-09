def main():
    # input
    N = int(input())
    LAs = [list(map(int, input().split())) for _ in range(N)]
    # compute
    Ls = [LAs[i][0] for i in range(N)]
    As = [LAs[i][1:] for i in range(N)]
    # output
    print(len(set(tuple(As[i]) for i in range(N))))
