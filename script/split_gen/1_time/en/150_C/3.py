def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    P = tuple(P)
    Q = tuple(Q)
    P = (P[0],) + P[1:] + (N + 1,)
    Q = (Q[0],) + Q[1:] + (N + 1,)
    # print(P)
    # print(Q)
    P_index = 0
    Q_index = 0
    for i in range(1, N + 1):
        # print("i", i)
        for j in range(1, N + 1):
            # print("j", j)
            if P[i] > P[j]:
                P_index += 1
            if Q[i] > Q[j]:
                Q_index += 1
    # print(P_index)
    # print(Q_index)
    print(abs(P_index - Q_index))
