def innerRating(N, R):
    if N >= 10:
        return R
    else:
        return R + 100 * (10 - N)

if __name__ == '__main__':
    innerRating()