def main():
    N,K=map(int,input().split())
    H=list(map(int,input().split()))
    H.sort(reverse=True)
    #print(H)
    if K>=N:
        print(0)
    else:
        print(sum(H[K:]))
main()
