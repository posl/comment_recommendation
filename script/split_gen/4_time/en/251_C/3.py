def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    max_score = 0
    best_submission = 0
    for i in range(N):
        if T[i] > max_score:
            max_score = T[i]
            best_submission = i
    print(best_submission + 1)
