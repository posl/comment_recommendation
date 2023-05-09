def problems175_c(x, k, d):
    if x < 0:
        x = -x
    if x//d >= k:
        return x - k*d
    else:
        x = x%d
        k -= x//d
        if k%2 == 0:
            return x
        else:
            return d-x
