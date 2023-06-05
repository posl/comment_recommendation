def main():
    N=int(input())
    uvw=[]
    for i in range(N-1):
        uvw.append([int(i) for i in input().split()])
    uvw.sort(key=lambda x:x[2])
    print(uvw)
    for i in range(N-1):
        for j in range(i+1,N):
            print(uvw[i],uvw[j])
            if uvw[i][0] in uvw[j] or uvw[i][1] in uvw[j]:
                print(uvw[i],uvw[j])
                uvw[i][2]=uvw[j][2]
    print(uvw)
    sum=0
    for i in range(N-1):
        sum+=uvw[i][2]
    print(sum)
