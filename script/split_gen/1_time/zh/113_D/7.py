def amidakuji(h,w,k):
    if w==1:
        return 1
    if k==1:
        return amidakuji(h,w-1,1)+amidakuji(h,w-1,2)
    if k==w:
        return amidakuji(h,w-1,w-1)+amidakuji(h,w-1,w)
    return amidakuji(h,w-1,k-1)+amidakuji(h,w-1,k)+amidakuji(h,w-1,k+1)
h,w,k=map(int,input().split())
print(amidakuji(h,w,k)%1000000007)
