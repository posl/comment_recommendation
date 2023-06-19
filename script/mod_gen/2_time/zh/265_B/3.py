def isReachable(N,M,T,A,X,Y):
    #print(N,M,T,A,X,Y)
    #print("N = ",N)
    #print("M = ",M)
    #print("T = ",T)
    #print("A = ",A)
    #print("X = ",X)
    #print("Y = ",Y)
    #print()
    if N == 1:
        return True
    if N == 2:
        if M == 0:
            return True
        else:
            return False
    if N == 3:
        if T >= A[0] + A[1]:
            return True
        else:
            if M == 0:
                return False
            else:
                if T >= A[0] + Y[0]:
                    return True
                else:
                    return False
    if N == 4:
        if T >= A[0] + A[1] + A[2]:
            return True
        else:
            if M == 0:
                return False
            else:
                if T >= A[0] + A[1] + Y[0]:
                    return True
                else:
                    if T >= A[0] + Y[0] + Y[1]:
                        return True
                    else:
                        if T >= A[0] + Y[0] + A[2]:
                            return True
                        else:
                            return False
    if N == 5:
        if T >= A[0] + A[1] + A[2] + A[3]:
            return True
        else:
            if M == 0:
                return False
            else:
                if T >= A[0] + A[1] + A[2] + Y[0]:
                    return True
                else:
                    if T >= A[0] + A[1] + Y[0] + Y[1]:
                        return True
                    else:
                        if T >= A[0] + A[1] + Y[0] + A[3]:
                            return True
                        else:
                            if T >= A[0] + Y[0] + Y[1] + Y[2]:
                                return True
                            else:
                                if T >= A[0] + Y[0] + Y[1] + A[3]:
                                    return

if __name__ == '__main__':
    isReachable()