def problem247_c(n):
    if n == 1:
        print(1)
        return
    s = [1]
    for i in range(2,n+1):
        s = s + [i] + s
    print(" ".join(map(str,s)))
    return
