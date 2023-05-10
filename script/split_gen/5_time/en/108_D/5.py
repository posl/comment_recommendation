def main():
    l = int(input())
    n = 0
    m = 0
    for i in range(20):
        if (l>>i)&1:
            n = i+1
            m = i
    print(n,m)
    for i in range(1,n):
        print(i,i+1,0)
        print(i,i+1,2**(i-1))
    for i in range(m-n+1):
        print(i+1,n,2**(m-i-1))
