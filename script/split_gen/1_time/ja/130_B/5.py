def main():
    # input
    N, X = map(int, input().split())
    Ls = list(map(int, input().split()))
    # compute
    Ds = [0]
    for i in range(N):
        Ds.append(Ds[-1]+Ls[i])
    # output
    print(sum([1 for D in Ds if D<=X]))
