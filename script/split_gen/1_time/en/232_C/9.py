def check(takahashi,aoki):
    for i in range(len(takahashi)):
        if takahashi[i] in aoki[i]:
            continue
        else:
            return False
    return True
