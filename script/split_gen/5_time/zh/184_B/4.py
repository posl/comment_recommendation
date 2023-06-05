def main():
    n,x=input().split()
    n=int(n)
    x=int(x)
    s=input()
    sum=x
    for i in range(n):
        if s[i]=='o':
            sum+=1
        elif s[i]=='x' and sum>0:
            sum-=1
    print(sum)
