def perm(l):
    if len(l) <= 1:
        yield l
    else:
        for i in range(len(l)):
            s = l[:i] + l[i+1:]
            for p in perm(s):
                yield l[i:i+1] + p

if __name__ == '__main__':
    perm()