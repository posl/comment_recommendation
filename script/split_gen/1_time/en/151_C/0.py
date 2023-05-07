def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    correct = 0
    penalty = 0
    AC = [False] * (N+1)
    WA = [0] * (N+1)
    for i in range(M):
        if not AC[p[i]]:
            if S[i] == "AC":
                AC[p[i]] = True
                correct += 1
                penalty += WA[p[i]]
            else:
                WA[p[i]] += 1
    print(correct, penalty)
