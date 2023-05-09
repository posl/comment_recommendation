def level(n,x):
    if n==0:
        return 1 if x>0 else 0
    if x==1:
        return 0
    if x<=1+level(n-1,0):
        return level(n-1,x-1)
    if x==2+level(n-1,0):
        return 1
    if x<=2+2*level(n-1,0):
        return 1+level(n-1,x-2-level(n-1,0))
    return 1+2*level(n-1,0)
n,x=map(int,input().split())
print(level(n,x))

if __name__ == '__main__':
    level()