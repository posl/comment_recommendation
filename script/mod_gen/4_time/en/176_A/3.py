def takoyaki(N,X,T):
    if N%X==0:
        return (N/X)*T
    else:
        return ((N//X)+1)*T

if __name__ == '__main__':
    takoyaki()