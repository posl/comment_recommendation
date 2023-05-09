def main():
    N, M = map(int, input().split())
    correct = 0
    penalty = 0
    p = [0] * (N + 1)
    for i in range(M):
        pi, si = input().split()
        pi = int(pi)
        if si == "AC":
            if p[pi] == 0:
                correct += 1
                p[pi] = 1
        else:
            if p[pi] == 0:
                penalty += 1
    print(correct, penalty)
