def main():
    n,a,b = map(int,input().split())
    p,q,r,s = map(int,input().split())
    n = n + 1
    a = a + 1
    b = b + 1
    p = p + 1
    q = q + 1
    r = r + 1
    s = s + 1
    for i in range(p,q):
        for j in range(r,s):
            if (i-a) == (j-b) or (i-a) == (b-j) or (a-i) == (j-b) or (a-i) == (b-j):
                print("#",end="")
            else:
                print(".",end="")
        print("")

if __name__ == '__main__':
    main()