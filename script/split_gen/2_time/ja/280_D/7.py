def main():
    K=int(input())
    #K=280
    #K=123456789011
    #K=30
    N=1
    while True:
        if N%K==0:
            break
        N=N+1
    print(N)
    return
