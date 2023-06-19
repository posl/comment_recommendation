def main():
    # read input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # sort A in descending order
    A.sort(reverse=True)
    
    # initialize
    A_idx = 0
    B_idx = 0
    
    # search
    while A_idx < N and B_idx < M:
        if A[A_idx] >= B[B_idx]:
            A_idx += 1
            B_idx += 1
        else:
            A_idx += 1
    
    # output
    if B_idx == M:
        print('Yes')
    else:
        print('No')
main()
