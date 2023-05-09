def main():
    #input
    a,b,c,d,e=map(int,input().split())
    #output
    print("Yes" if (a==b==c and d==e and a!=d) or (a==b and c==d==e and a!=c) else "No")
