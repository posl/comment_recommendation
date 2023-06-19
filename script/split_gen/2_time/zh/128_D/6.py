def max_sum(n,k,v):
    if n == k:
        return sum(v)
    if k == 0:
        return 0
    if n == 1:
        return max(v[0],0)
    if k == 1:
        return max(v[0],v[-1],0)
    if n == 2:
        return max(v[0]+v[1],v[0],v[1],0)
    if k == 2:
        return max(v[0]+v[1],v[0]+v[-1],v[-1]+v[-2],v[0],v[1],v[-1],v[-2],0)
    if n == 3:
        return max(v[0]+v[1]+v[2],v[0]+v[1],v[0]+v[2],v[1]+v[2],v[0],v[1],v[2],0)
    if k == 3:
        return max(v[0]+v[1]+v[2],v[0]+v[1]+v[-1],v[0]+v[-2]+v[-1],v[-3]+v[-2]+v[-1],v[0]+v[1],v[0]+v[2],v[1]+v[2],v[0]+v[-1],v[-1]+v[-2],v[-2]+v[-3],v[0],v[1],v[2],v[-1],v[-2],v[-3],0)
    if n == 4:
        return max(v[0]+v[1]+v[2]+v[3],v[0]+v[1]+v[2],v[0]+v[1]+v[3],v[0]+v[2]+v[3],v[1]+v[2]+v[3],v[0]+v[1],v[0]+v[2],v[0]+v[3],v[1]+v[2],v[1]+v[3],v[2]+v[3],v[0],v[1],v[2],v[3],0)
    if k == 4:
        return max(v[0]+v[1]+v[2]+v
