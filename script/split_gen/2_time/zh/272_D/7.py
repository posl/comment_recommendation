def main():
    n,m = map(int,input().split())
    m = m**0.5
    m = int(m)
    #print(m)
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                print(0,end=' ')
            elif i==0:
                print(j,end=' ')
            elif j==0:
                print(i,end=' ')
            else:
                print(m,end=' ')
        print()
