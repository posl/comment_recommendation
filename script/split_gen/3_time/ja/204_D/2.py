def func(n, t):
    if n == 1:
        return t[0]
    if n == 2:
        return max(t[0], t[1])
    if n == 3:
        return max(t[0]+t[1], t[2])
    if n == 4:
        return max(t[0]+t[3], t[1]+t[2])
    if n == 5:
        return max(t[0]+t[3]+t[4], t[1]+t[2]+t[4])
    if n == 6:
        return max(t[0]+t[3]+t[5], t[1]+t[2]+t[5], t[0]+t[1]+t[2]+t[3]+t[4]+t[5])
    if n == 7:
        return max(t[0]+t[3]+t[6], t[1]+t[2]+t[6], t[0]+t[1]+t[2]+t[3]+t[4]+t[6])
    if n == 8:
        return max(t[0]+t[3]+t[7], t[1]+t[2]+t[7], t[0]+t[1]+t[2]+t[3]+t[4]+t[7], t[0]+t[1]+t[2]+t[3]+t[5]+t[6])
    if n == 9:
        return max(t[0]+t[3]+t[8], t[1]+t[2]+t[8], t[0]+t[1]+t[2]+t[3]+t[4]+t[8], t[0]+t[1]+t[2]+t[3]+t[5]+t[8], t[0]+t[1]+t[2]+t[3]+t[6]+t[7])
