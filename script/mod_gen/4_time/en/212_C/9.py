def find_min_diff(A, B):
    A.sort()
    B.sort()
    min_diff = 10**9
    for a in A:
        for b in B:
            diff = abs(a-b)
            if diff < min_diff:
                min_diff = diff
            else:
                break
    return min_diff

if __name__ == '__main__':
    find_min_diff()