def base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(str(X)[-i]) * (n**(i-1))
    return out
