def main():
    n,a,b = map(int,input().split())
    for i in range(n*a):
        if i%a == 0:
            for j in range(n*b):
                if j%b == 0:
                    print("#",end="")
                else:
                    print(".",end="")
            print("")
        else:
            for j in range(n*b):
                if j%b == 0:
                    print(".",end="")
                else:
                    print("#",end="")
            print("")

if __name__ == '__main__':
    main()