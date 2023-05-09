def solve(N, M, A):
    from collections import Counter
    A = [a % M for a in A]
    C = Counter(A)
    if M == 2:
        return min(C[0], C[1])
    if M == 3:
        return min(C[0], C[1], C[2])
    if M == 4:
        return min(C[0] + C[2], C[1] + C[3])
    if M == 5:
        return min(C[0] + C[3], C[1] + C[4], C[2])
    if M == 6:
        return min(C[0] + C[2] + C[4], C[1] + C[3] + C[5])
    if M == 7:
        return min(C[0] + C[3] + C[6], C[1] + C[4], C[2] + C[5])
    if M == 8:
        return min(C[0] + C[2] + C[4] + C[6], C[1] + C[3] + C[5] + C[7])
    if M == 9:
        return min(C[0] + C[3] + C[6], C[1] + C[4] + C[7], C[2] + C[5] + C[8])
    if M == 10:
        return min(C[0] + C[2] + C[4] + C[6] + C[8], C[1] + C[3] + C[5] + C[7] + C[9])
    if M == 11:
        return min(C[0] + C[3] + C[6] + C[9], C[1] + C[4] + C[7], C[2] + C[5] + C[8] + C[10])
    if M == 12:
        return min(C[0] + C[2] + C[4] + C[6] + C[8] + C[10], C[1] + C[3] + C[5] + C[7] + C[9] + C[11])
