def solution(k):
    if k%2 == 0 or k%5 == 0:
        return -1
    else:
        if k == 1:
            return 1
        else:
            n = 1
            x = 7
            while True:
                if x%k == 0:
                    return n
                else:
                    n += 1
                    x = x*10 + 7
    return -1
