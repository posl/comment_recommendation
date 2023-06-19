def func(N,K):
    for i in range(K):
        if N%200==0:
            N=N//200
        else:
            N=str(N)
            N=N+'200'
            N=int(N)
    return N

if __name__ == '__main__':
    func()