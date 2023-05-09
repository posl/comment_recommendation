def countRGB(s, s_len):
    count_r = 0
    count_g = 0
    count_b = 0
    for i in range(s_len):
        if s[i] == "R":
            count_r += 1
        elif s[i] == "G":
            count_g += 1
        elif s[i] == "B":
            count_b += 1
    return count_r, count_g, count_b
