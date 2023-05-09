def main():
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)
    correct = 0
    penalty = 0
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        if S[i] == "AC":
            if AC[p[i]-1] == 0:
                AC[p[i]-1] = 1
                correct += 1
                penalty += WA[p[i]-1]
        else:
            WA[p[i]-1] += 1
    print(correct, penalty)
