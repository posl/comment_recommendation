def calc(a,b):
    cnt = 0
    while True:
        if b <= a:
            break
        b -= (a-1)
        cnt += 1
    return cnt
