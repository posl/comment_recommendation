def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. A[i] + A[i+1] + ... + A[j] = S[j] - S[i-1]
    # 2. sum_{i=1}^{M} i × B_i = M × (M+1) / 2 + (S[j] - S[i-1]) × (M+1)
    # 3. sum_{i=1}^{M} i × B_i = M × (M+1) / 2 + (S[j] - S[i-1]) × (M+1) - M × (M+1) / 2 = (S[j] - S[i-1]) × (M+1)
    # 4. sum_{i=1}^{M} i × B_i = (S[j] - S[i-1]) × (M+1)
    # 5. sum_{i=1}^{M} i × B_i = S[j] × (M+1) - S[i-1] × (M+1)
    # 6. sum_{i=1}^{M} i × B_i = S[j] × (M+1) - S[i-1] × (M+1) + M × (M+1) / 2
    # 7. sum_{i=1}^{M} i × B_i = S[j] × (M+1) - S[i-1] × (M+1) + M × (M+1) / 2 - M × (M+1) / 2 = S[j] × (M+1) - S[i-1] × (M+1)
    # 8. sum_{i=1}^{M} i × B_i = (S[j] - S[i-1]) × (M+1)
    # 9. sum_{i=1}^{M} i × B_i = (S[j] - S[i-1]) × (M+1) + S[i-1] × (M+1) - S[j] × (M+1)
    #10. sum_{i=1}^{M} i × B_i = (S[j]
