def f(n,k,vs):
    if k==0:
        return 0
    if n==0:
        return 0
    if n==1:
        return vs[0]
    if n==2:
        return max(vs[0],vs[1])
    if n==3:
        return max(vs[0],vs[1],vs[2])
    if n==4:
        return max(vs[0]+vs[3],vs[1]+vs[2])
    if n==5:
        return max(vs[0]+vs[3],vs[1]+vs[2],vs[0]+vs[4],vs[1]+vs[3],vs[2]+vs[3],vs[3]+vs[4])
    if n==6:
        return max(vs[0]+vs[3]+vs[5],vs[1]+vs[2]+vs[4],vs[0]+vs[4]+vs[5],vs[0]+vs[1]+vs[3],vs[1]+vs[2]+vs[3],vs[2]+vs[3]+vs[4],vs[3]+vs[4]+vs[5])
    if n==7:
        return max(vs[0]+vs[3]+vs[5],vs[1]+vs[2]+vs[4],vs[0]+vs[4]+vs[5],vs[0]+vs[1]+vs[3]+vs[6],vs[1]+vs[2]+vs[3]+vs[5],vs[2]+vs[3]+vs[4]+vs[6],vs[3]+vs[4]+vs[5]+vs[6],vs[0]+vs[3]+vs[4]+vs[6],vs[1]+vs[2]+vs[5]+vs[6],vs[2]+vs[4]+vs[5]+vs[6],vs[0]+vs[1]+vs[2]+vs[3],vs[1]+vs[2]+vs[3]+vs[4],vs[2]+vs[3]+vs[4]+vs[5],vs[3]+vs[4]+vs[5]+vs[6])
    if n==8:
        return max(vs[0]+vs[3]+vs[5]+vs[7],vs

if __name__ == '__main__':
    f()