def nextConfusingTime(H,M):
    #print(H,M)
    if H>23 or M>59:
        return "Invalid Input"
    if H==23 and M==59:
        return "00 00"
    if H==0 and M==0:
        return "00 00"
    if M==59:
        H+=1
        M=0
    else:
        M+=1
    #print(H,M)
    if H<10:
        H="0"+str(H)
    else:
        H=str(H)
    if M<10:
        M="0"+str(M)
    else:
        M=str(M)
    #print(H,M)
    if H[0]==M[1] and H[1]==M[0]:
        return H+" "+M
    else:
        return nextConfusingTime(int(H),int(M))
H,M=map(int,input().split())
print(nextConfusingTime(H,M))
