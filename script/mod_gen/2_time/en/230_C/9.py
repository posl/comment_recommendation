def find_squares(n,a,b,p,q,r,s):
    if n == 1:
        if a == 1 and b == 1:
            return [1]
        else:
            return [0]
    if a == 1 and b == 1:
        return [1] + [0]*(n-1)
    elif a == 1 and b == n:
        return [0]*(n-1) + [1]
    elif a == n and b == 1:
        return [0]*(n-1) + [1]
    elif a == n and b == n:
        return [1] + [0]*(n-1)
    else:
        if p <= a+b-2 and q >= a+b-2 and r <= a-b+2*n-2 and s >= a-b+2*n-2:
            return [1] + [0]*(n-1)
        elif p <= a+b-2 and q >= a+b-2:
            return [1] + find_squares(n-1,a,b-1,p,q,r,s)
        elif r <= a-b+2*n-2 and s >= a-b+2*n-2:
            return [1] + find_squares(n-1,a-1,b,p,q,r,s)
        else:
            return [0] + find_squares(n-1,a-1,b-1,p,q,r,s)
n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())
print('\n'.join([''.join([['.','\#'][i] for i in find_squares(n,a,b,p+k,q+k,r+k,s+k)]) for k in range(q-p+1)]))

if __name__ == '__main__':
    find_squares()