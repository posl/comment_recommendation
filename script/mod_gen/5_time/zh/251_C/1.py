def get_best_submission(N, S, T):
    best_score = -1
    best_submission = -1
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_submission = i
    best_submissions = []
    for i in range(N):
        if T[i] == best_score:
            best_submissions.append(i)
    best_submission = best_submissions[0]
    for i in range(len(best_submissions)):
        if S[best_submissions[i]] < S[best_submission]:
            best_submission = best_submissions[i]
    return best_submission + 1
N = int(input())
S = []
T = []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
print(get_best_submission(N, S, T))
