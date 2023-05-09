def rating(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)
n, r = map(int, input().split())
print(rating(n, r))

if __name__ == '__main__':
    rating()