def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(A):
            for k in range(N):
                for l in range(B):
                    if i%2 == 0 and k%2 == 0:
                        print(".",end="")
                    elif i%2 == 0 and k%2 == 1:
                        print("#",end="")
                    elif i%2 == 1 and k%2 == 0:
                        print("#",end="")
                    elif i%2 == 1 and k%2 == 1:
                        print(".",end="")
                print("",end="")
            print("")
        print("")
