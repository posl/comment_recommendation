def get_min_time(P, Q, R):
    min_time = P + Q
    if min_time > Q + R:
        min_time = Q + R
    if min_time > R + P:
        min_time = R + P
    return min_time
