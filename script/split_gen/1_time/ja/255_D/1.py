def main():
    # input
    N, Q = map(int, input().split())
    As = [*map(int, input().split())]
    Xs = [*map(int, input().split())]
    # compute
    ans = []
    for X in Xs:
        ans.append(sum(abs(A-X) for A in As))
    # output
    for a in ans:
        print(a)
