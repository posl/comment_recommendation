def solve(X,A,D,N):
    if N==1:
        return 0
    if D==0:
        if X==A:
            return 0
        else:
            return 1
    if N%2==0:
        if X%2==0:
            if (X-A)%D==0:
                return 0
            else:
                return 1
        else:
            return 1
    else:
        if X%2==0:
            return 1
        else:
            if (X-A)%D==0:
                return 0
            else:
                return 1
