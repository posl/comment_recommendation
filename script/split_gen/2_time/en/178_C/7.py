def solve(n):
    return (pow(10,n,mod) - 2*pow(9,n,mod) + pow(8,n,mod))%mod
