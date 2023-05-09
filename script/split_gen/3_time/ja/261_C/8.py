def main():
    N=int(input())
    S=[input() for i in range(N)]
    d={}
    for s in S:
        if s in d:
            d[s]+=1
        else:
            d[s]=1
    for s in S:
        if d[s]==1:
            print(s)
        else:
            print(s+"("+str(d[s]-1)+")")
