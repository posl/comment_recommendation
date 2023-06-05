def solve(a,b,t):
    count=0
    for i in range(1,t+1):
        if i%a==0:
            count+=b
    return count

if __name__ == '__main__':
    solve()