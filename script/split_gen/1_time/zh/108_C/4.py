def get_num(N,K):
    count = 0
    for a in range(1,N+1):
        if a % K == 0:
            for b in range(1,N+1):
                if b % K == 0:
                    for c in range(1,N+1):
                        if c % K == 0:
                            if (a+b)%K == 0 and (b+c)%K == 0 and (c+a)%K == 0:
                                count += 1
    return count
