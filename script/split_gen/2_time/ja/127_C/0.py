def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L_max = max(L)
    R_min = min(R)
    if R_min >= L_max:
        print(R_min - L_max + 1)
    else:
        print(0)
