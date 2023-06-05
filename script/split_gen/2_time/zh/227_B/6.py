def get_last_person(n,k,a):
    if a + k <= n:
        return a + k - 1
    else:
        return a + k - n - 1
