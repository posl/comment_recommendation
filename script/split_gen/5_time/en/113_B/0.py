def main():
    # input
    N = int(input())
    T, A = map(int, input().split())
    Hs = list(map(int, input().split()))
    # compute
    diffs = []
    for H in Hs:
        diffs.append(abs(A - (T - H * 0.006)))
    # output
    print(diffs.index(min(diffs)) + 1)
