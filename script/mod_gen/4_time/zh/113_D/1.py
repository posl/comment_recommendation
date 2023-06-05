def amidakuji(H,W,K):
    if H==1:
        return 1
    if K==1:
        return 2**(W-1)
    if K==W:
        return 2**(W-1)
    return amidakuji(H-1,W-1,K-1)+amidakuji(H-1,W,K-1)

if __name__ == '__main__':
    amidakuji()