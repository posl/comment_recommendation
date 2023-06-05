def main():
    n,a,b = map(int,input().split())
    for i in range(a*n):
        for j in range(b*n):
            if i%2==0:
                if j%2==0:
                    print(".",end="")
                else:
                    print("#",end="")
            else:
                if j%2==0:
                    print("#",end="")
                else:
                    print(".",end="")
        print("")
