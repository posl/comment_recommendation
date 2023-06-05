def get_min_count(N):
    if N == 0:
        return 0
    if N < 6:
        return N
    if N < 9:
        return N-1
    if N == 9:
        return 1
    if N < 36:
        return min(1+get_min_count(N-9), N-1)
    if N == 36:
        return 1
    if N < 81:
        return min(1+get_min_count(N-36), 1+get_min_count(N-9), N-1)
    if N == 81:
        return 1
    if N < 216:
        return min(1+get_min_count(N-81), 1+get_min_count(N-36), 1+get_min_count(N-9), N-1)
    if N == 216:
        return 1
    if N < 729:
        return min(1+get_min_count(N-216), 1+get_min_count(N-81), 1+get_min_count(N-36), 1+get_min_count(N-9), N-1)
    if N == 729:
        return 1
    if N < 1296:
        return min(1+get_min_count(N-729), 1+get_min_count(N-216), 1+get_min_count(N-81), 1+get_min_count(N-36), 1+get_min_count(N-9), N-1)
    if N == 1296:
        return 1
    if N < 6561:
        return min(1+get_min_count(N-1296), 1+get_min_count(N-729), 1+get_min_count(N-216), 1+get_min_count(N-81), 1+get_min_count(N-36), 1+get_min_count(N-9), N-1)
    if N == 6561:
        return 1
    if N < 7776:
        return min(1+get_min_count(N-6561), 1+get_min_count(N-1296), 1+get_min_count(N-729), 1+get_min_count(N-216), 1+get_min_count(N-81), 1+get_min_count(N-36), 1+
