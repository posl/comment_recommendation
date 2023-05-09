def innerRating(N, R):
    if N >= 10:
        return R
    else:
        return R + 100 * (10 - N)
