def main():
    n,a,b = map(int,input().split())
    p,q,r,s = map(int,input().split())
    a,b = a-1,b-1
    for i in range(p,q+1):
        for j in range(r,s+1):
            if (i-a) == (j-b):
                print("#",end="")
            elif (i-a) == -(j-b):
                print("#",end="")
            else:
                print(".",end="")
        print()
