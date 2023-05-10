def cooking_time(n, t):
    if n == 1:
        return t[0]
    elif n == 2:
        return max(t[0], t[1])
    else:
        oven1 = t[0]
        oven2 = t[1]
        for i in range(2, n):
            if oven1 <= oven2:
                oven1 += t[i]
            else:
                oven2 += t[i]
        return max(oven1, oven2)
