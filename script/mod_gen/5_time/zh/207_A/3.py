def max_sum(a,b,c):
    if a >= b and a >= c:
        return a + max(b,c)
    elif b >= a and b >= c:
        return b + max(a,c)
    else:
        return c + max(a,b)

if __name__ == '__main__':
    max_sum()