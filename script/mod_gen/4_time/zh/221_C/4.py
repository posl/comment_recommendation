def split(n):
    s=str(n)
    l=len(s)
    if l==1:
        return n
    if l==2:
        return n
    if l==3:
        return max(n//10,n%10)*max(n//10,n%10)*max(n//10,n%10)
    if l==4:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==5:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==6:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==7:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==8:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==9:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==10:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
n=int(input())
print(split(n))
