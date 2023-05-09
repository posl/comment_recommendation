def lower_case_kth_char(S, K):
    return S[:K-1] + S[K-1].lower() + S[K:]

if __name__ == '__main__':
    lower_case_kth_char()