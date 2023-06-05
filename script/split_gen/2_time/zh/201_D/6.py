def count_passwords(s):
    count = 0
    for i in range(10000):
        password = str(i).zfill(4)
        if all([password[int(c)] == s[int(c)] for c in range(10) if s[int(c)] != '?']):
            count += 1
    return count
