def S(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
K=int(input())
n=1
while K>0:
    if n%S(n)==0:
        print(n)
        K-=1
    n+=1

if __name__ == '__main__':
    S()