def paint_pattern(n,a,b):
    if n==1:
        for i in range(2*a):
            print("#"*b)
    else:
        for i in range(a):
            print("#"*b,end="")
            for j in range(n-1):
                print("."*b,end="")
                print("#"*b,end="")
            print("")

if __name__ == '__main__':
    paint_pattern()