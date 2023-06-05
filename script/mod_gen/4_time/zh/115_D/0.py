def solve(n,x):
    if n==0:
        return 0 if x<=0 else 1
    num_layer=3*(2**n-1)+1
    num_patty=2**(n+1)-1
    if x==1:
        return 0
    elif x==num_layer:
        return num_patty
    elif x<=1+num_layer//2:
        return solve(n-1,x-1)
    else:
        return num_patty//2+1+solve(n-1,x-2-(num_layer//2))

if __name__ == '__main__':
    solve()