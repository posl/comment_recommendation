def main():
    K = int(input())
    #print("K=",K)
    #print("1<<K=",1<<K)
    #print("bin(1<<K)=",bin(1<<K))
    #print("bin(1<<K)[3:]=",bin(1<<K)[3:])
    #print("bin(1<<K)[3:-1]=",bin(1<<K)[3:-1])
    #print("int(bin(1<<K)[3:-1],2)=",int(bin(1<<K)[3:-1],2))
    print("2" + bin(1<<K)[3:-1] + "2")
