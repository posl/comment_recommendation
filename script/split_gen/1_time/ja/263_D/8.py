def main():
    N,L,R=map(int,input().split())
    A=list(map(int,input().split()))
    #print(N,L,R,A)
    S=sum(A)
    #print(S)
    #print("max",max(A))
    #print("min",min(A))
    #print("max-min",max(A)-min(A))
    #print("sum",sum(A))
    #print("max-min-sum",max(A)-min(A)+sum(A))
    #print("max-min-sum/2",int((max(A)-min(A)+sum(A))/2))
    #print("max-min-sum/2+min",int((max(A)-min(A)+sum(A))/2)+min(A))
    #print("max-min-sum/2+min-max",int((max(A)-min(A)+sum(A))/2)+min(A)-max(A))
    if L==R:
        print(N*L)
    elif L>R:
        if max(A)-min(A)+sum(A) >= 0:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A))
        else:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A)+N*R)
    else:
        if max(A)-min(A)+sum(A) >= 0:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A))
        else:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A)+N*L)
