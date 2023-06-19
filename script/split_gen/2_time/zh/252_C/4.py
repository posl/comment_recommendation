def get_min_time(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    if s1 == s2:
        return 0
    else:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count
