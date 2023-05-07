def solve(N):
    count = 0
    for a in range(1,N+1):
        if a**2 > N:
            break
        for b in range(a,N+1):
            if a*b > N:
                break
            count += (N//(a*b))
    return count

if __name__ == '__main__':
    solve()