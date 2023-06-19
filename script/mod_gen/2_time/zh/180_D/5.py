def solve(X,Y,A,B):
    exp=0
    while X*A<X+B and X*A<Y:
        X*=A
        exp+=1
    exp+=(Y-X-1)//B
    return exp

if __name__ == '__main__':
    solve()