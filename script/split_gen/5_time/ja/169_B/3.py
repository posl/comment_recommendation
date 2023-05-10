def main():
    # input
    N = int(input())
    A_list = list(map(int, input().split()))
    # compute
    A = 1
    for i in range(N):
        A *= A_list[i]
    # output
    if A > 10**18:
        print(-1)
    else:
        print(A)
