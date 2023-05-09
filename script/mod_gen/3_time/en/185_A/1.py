def get_max_contests(A_1, A_2, A_3, A_4):
    contests = 0
    if A_1 > 0:
        contests += 1
    if A_2 > 0:
        contests += 1
    if A_3 > 0:
        contests += 1
    if A_4 > 0:
        contests += 1
    return contests

if __name__ == '__main__':
    get_max_contests()