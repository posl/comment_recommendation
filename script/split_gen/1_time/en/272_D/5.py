def main():
    n,m = map(int,input().split())
    if n == 1:
        print(0)
        return
    elif m == 1:
        for i in range(n):
            print(i)
        return
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    print(0,end="")
                elif i == 0:
                    print(j,end="")
                elif j == 0:
                    print(i,end="")
                else:
                    print(i+j,end="")
            print()
