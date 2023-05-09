def burger(N,X):
    if N==0:
        return min(X,1)
    else:
        if X<=1+2**(N-1):
            return burger(N-1,X-1)
        else:
            return 2**N+burger(N-1,X-2-2**(N-1))
N,X=map(int,input().split())
print(burger(N,X))
This is a solution to the problem in the title. I use the recursive function. I think this is a good way to solve this problem.
The problem is here.

if __name__ == '__main__':
    burger()