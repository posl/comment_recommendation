def getNums(s, t):
    num = 0
    for i in range(s+1):
        for j in range(s+1):
            for k in range(s+1):
                if i+j+k <= s and i*j*k <= t:
                    num += 1
    return num
