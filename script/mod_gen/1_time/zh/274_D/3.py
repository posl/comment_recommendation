def solve(n,x,y,A):
    for i in range(n):
        for j in range(i+1,n):
            if abs(A[i]-A[j]) == abs(x-y):
                return True
    return False

if __name__ == '__main__':
    solve()