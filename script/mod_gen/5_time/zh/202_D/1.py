def dfs(a,b,k):
    if a == 0:
        return 'b'*b
    if b == 0:
        return 'a'*a
    if k <= 2**(a+b-1):
        return 'a' + dfs(a-1,b,k)
    else:
        return 'b' + dfs(a,b-1,k-2**(a+b-1))

if __name__ == '__main__':
    dfs()