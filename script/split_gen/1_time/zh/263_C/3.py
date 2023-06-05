def print_all_sequences(n, m, a):
    if n == 0:
        print(a)
        return
    for i in range(1, m+1):
        if len(a) > 0 and i <= a[-1]:
            continue
        a.append(i)
        print_all_sequences(n-1, m, a)
        a.pop()
