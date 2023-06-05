def solve(s1, s2, s3):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        return False
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            if i + j == int(s3):
                if check(s1, i) and check(s2, j) and check(s3, i + j):
                    return [i, j, i + j]
    return False

if __name__ == '__main__':
    solve()