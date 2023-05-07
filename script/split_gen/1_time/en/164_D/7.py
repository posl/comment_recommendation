def count_mod_2019(s):
    if len(s) < 4:
        if int(s) % 2019 == 0:
            return 1
        else:
            return 0
    else:
        count = 0
        for i in range(0, len(s) - 3):
            for j in range(i + 4, len(s) + 1):
                if int(s[i:j]) % 2019 == 0:
                    count += 1
        return count
