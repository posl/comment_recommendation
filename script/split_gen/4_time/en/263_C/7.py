def print_all_increasing_sequences(n, m, s="", i=1):
    if len(s) == n:
        print(s)
        return
    while i <= m:
        print_all_increasing_sequences(n, m, s + str(i), i + 1)
        i += 1
    return
