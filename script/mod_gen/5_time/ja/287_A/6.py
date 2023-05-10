def check_majority(n, s):
    for_count = 0
    against_count = 0
    for i in range(n):
        if s[i] == 'For':
            for_count += 1
        elif s[i] == 'Against':
            against_count += 1
    if for_count > against_count:
        return True
    else:
        return False

if __name__ == '__main__':
    check_majority()