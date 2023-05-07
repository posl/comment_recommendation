def solve(n,x,s):
    for i in range(n):
        if s[i]=='U':
            x=x//2
        elif s[i]=='L':
            x=2*x-1
        else:
            x=2*x+1
    return x
n,x=map(int,input().split())
s=input()
print(solve(n,x,s))

if __name__ == '__main__':
    solve()