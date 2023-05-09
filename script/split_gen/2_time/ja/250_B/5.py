def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i%2==0 and k%2==0) or (i%2==1 and k%2==1):
                        print("#",end="")
                    else:
                        print(".",end="")
                #print("")
            print("")
        #print("")
    #print("")
