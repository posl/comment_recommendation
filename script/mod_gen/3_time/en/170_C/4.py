def find_nearest(X, p):
    if len(p) == 0:
        return X
    else:
        p.sort()
        if X < p[0]:
            return p[0]
        elif X > p[-1]:
            return p[-1]
        else:
            for i in range(len(p) - 1):
                if p[i] < X < p[i + 1]:
                    if X - p[i] <= p[i + 1] - X:
                        return p[i]
                    else:
                        return p[i + 1]

if __name__ == '__main__':
    find_nearest()