def check_shiritori(n, words):
    if len(words) != n:
        return False
    if len(set(words)) != n:
        return False
    for i in range(1, n):
        if words[i][0] != words[i - 1][-1]:
            return False
    return True

if __name__ == '__main__':
    check_shiritori()