def num_of_patty(n):
    if n==0:
        return 0
    else:
        return 2*num_of_patty(n-1)+1
