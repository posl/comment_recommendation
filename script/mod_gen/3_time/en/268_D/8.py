def check(x, M, T):
    for i in range(M):
        if x.find(T[i]) != -1:
            return False
    return True

if __name__ == '__main__':
    check()