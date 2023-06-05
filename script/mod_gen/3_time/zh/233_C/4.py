def solve(N,X,L,A):
    import itertools
    def product(A):
        import functools
        return functools.reduce(lambda x,y:x*y,A)
    def count(A,X):
        return sum(product(a) == X for a in itertools.product(*A))
    return count(A,X)

if __name__ == '__main__':
    solve()