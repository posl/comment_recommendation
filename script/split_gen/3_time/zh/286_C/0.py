def main():
    n,a,b = map(int,input().split())
    s = input()
    s1 = s[::-1]
    if s == s1:
        print(a*n+b*(n-1))
    else:
        s2 = s1[::-1]
        s3 = s2[0:n//2]
        if s3 == s:
            print(a*n+b*(n-1))
        else:
            s4 = s3[::-1]
            s5 = s2[n//2+1:n]
            if s4 == s5:
                print(a*n+b*(n-1))
            else:
                print(a*n+b*n)
