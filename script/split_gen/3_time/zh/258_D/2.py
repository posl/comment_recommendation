def main():
    n,x=map(int,input().split())
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=map(int,input().split())
    a_b=[0]*n
    for i in range(n):
        a_b[i]=a[i]+b[i]
    #print(a_b)
    max_time=max(a_b)
    #print(max_time)
    max_time_index=a_b.index(max_time)
    #print(max_time_index)
    if x==1:
        print(max_time)
        return
    if max_time_index==n-1:
        print(max_time*x)
        return
    if x==2:
        print(max_time*2)
        return
    if max_time_index==0:
        print(max_time*x)
        return
    if x==3:
        print(max_time*2)
        return
    if max_time_index==1:
        print(max_time*2)
        return
    if x==4:
        print(max_time*2)
        return
    if max_time_index==2:
        print(max_time*2)
        return
    if x==5:
        print(max_time*2)
        return
    if max_time_index==3:
        print(max_time*2)
        return
    if x==6:
        print(max_time*2)
        return
    if max_time_index==4:
        print(max_time*2)
        return
    if x==7:
        print(max_time*2)
        return
    if max_time_index==5:
        print(max_time*2)
        return
    if x==8:
        print(max_time*2)
        return
    if max_time_index==6:
        print(max_time*2)
        return
    if x==9:
        print(max_time*2)
        return
    if max_time_index==7:
        print(max_time*2)
        return
    if x==10:
        print(max_time*2)
        return
    if max_time_index==8:
        print(max_time*2)
        return
    if x==11:
        print(max_time*2)
        return
    if max_time_index==9:
        print(max_time*2)
        return
    if x==12:
        print(max_time*2)
        return
    if max_time
