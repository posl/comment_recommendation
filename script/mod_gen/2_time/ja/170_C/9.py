def get_answer(X, N, p):
    if N == 0:
        return X
    else:
        i = 0
        while True:
            if X-i not in p:
                return X-i
            elif X+i not in p:
                return X+i
            else:
                i += 1

if __name__ == '__main__':
    get_answer()