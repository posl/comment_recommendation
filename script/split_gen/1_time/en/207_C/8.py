def main():
    N=int(input())
    left=[0]*N
    right=[0]*N
    for i in range(N):
        t,l,r=map(int,input().split())
        if t==1:
            left[i]=l
            right[i]=r
        elif t==2:
            left[i]=l
            right[i]=r-1
        elif t==3:
            left[i]=l+1
            right[i]=r
        else:
            left[i]=l+1
            right[i]=r-1
    count=0
    for i in range(N-1):
        for j in range(i+1,N):
            if left[i]<=right[j] and left[j]<=right[i]:
                count+=1
    print(count)
