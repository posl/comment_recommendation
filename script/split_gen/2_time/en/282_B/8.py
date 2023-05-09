def get_input():
    input_list = input().split()
    N = int(input_list[0])
    M = int(input_list[1])
    S = []
    for i in range(N):
        S.append(input())
    return N, M, S
