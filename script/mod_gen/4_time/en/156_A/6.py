def innerRating(n,r):
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))
innerRating(2,2919)
innerRating(22,3051)

if __name__ == '__main__':
    innerRating()