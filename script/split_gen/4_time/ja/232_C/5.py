def func(n, m, ab, cd):
    if n == 1:
        return "Yes"
    if m == 0:
        return "No"
    if m == 1:
        return "Yes"
    if m == 2:
        return "Yes" if ab[0][0] != ab[1][0] else "No"
    if m == 3:
        return "Yes" if ab[0][0] != ab[1][0] and ab[0][0] != ab[2][0] and ab[1][0] != ab[2][0] else "No"
    if m == 4:
        return "Yes" if ab[0][0] != ab[1][0] and ab[0][0] != ab[2][0] and ab[0][0] != ab[3][0] and ab[1][0] != ab[2][0] and ab[1][0] != ab[3][0] and ab[2][0] != ab[3][0] else "No"
    if m == 5:
        return "Yes" if ab[0][0] != ab[1][0] and ab[0][0] != ab[2][0] and ab[0][0] != ab[3][0] and ab[0][0] != ab[4][0] and ab[1][0] != ab[2][0] and ab[1][0] != ab[3][0] and ab[1][0] != ab[4][0] and ab[2][0] != ab[3][0] and ab[2][0] != ab[4][0] and ab[3][0] != ab[4][0] else "No"
    if m == 6:
        return "Yes" if ab[0][0] != ab[1][0] and ab[0][0] != ab[2][0] and ab[0][0] != ab[3][0] and ab[0][0] != ab[4][0] and ab[0][0] != ab[5][0] and ab[1][0] != ab[2][0] and ab[1][0] != ab[3][0] and
