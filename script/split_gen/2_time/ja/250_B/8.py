def main():
    n,a,b = map(int,input().split())
    for i in range(n):
        if i%2==0:
            for j in range(a):
                if j%2==0:
                    for k in range(b):
                        if k%2==0:
                            print(".",end="")
                        else:
                            print("#",end="")
                else:
                    for k in range(b):
                        if k%2==0:
                            print("#",end="")
                        else:
                            print(".",end="")
                print("")
        else:
            for j in range(a):
                if j%2==0:
                    for k in range(b):
                        if k%2==0:
                            print("#",end="")
                        else:
                            print(".",end="")
                else:
                    for k in range(b):
                        if k%2==0:
                            print(".",end="")
                        else:
                            print("#",end="")
                print("")
