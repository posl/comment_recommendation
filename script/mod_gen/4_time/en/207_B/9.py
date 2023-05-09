def solve(A,B,C,D):
    if A<=B*D:
        return -1
    else:
        return (A+B-1)//B

if __name__ == '__main__':
    solve()