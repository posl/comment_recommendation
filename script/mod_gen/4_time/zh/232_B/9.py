def f(S,T):
    for i in range(26):
        if S==T:
            return True
        else:
            S=S[-1]+S[:-1]
    return False

if __name__ == '__main__':
    f()