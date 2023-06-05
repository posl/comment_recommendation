def check(s1, s2, M):
    for i in range(M):
        if s1[i] == 'x' and s2[i] == 'x':
            return False
    return True

if __name__ == '__main__':
    check()