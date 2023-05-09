def main():
    # input
    N = int(input())
    Bs = list(map(int, input().split()))
    # compute
    As = [0] * N
    As[0] = Bs[0]
    As[-1] = Bs[-1]
    for i in range(N-2):
        As[i+1] = min(Bs[i], Bs[i+1])
    # output
    print(sum(As))
