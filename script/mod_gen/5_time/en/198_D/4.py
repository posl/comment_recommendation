def solve(S1, S2, S3):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                S1 = S1.replace('A', str(i))
                S1 = S1.replace('B', str(j))
                S1 = S1.replace('C', str(k))
                S2 = S2.replace('A', str(i))
                S2 = S2.replace('B', str(j))
                S2 = S2.replace('C', str(k))
                S3 = S3.replace('A', str(i))
                S3 = S3.replace('B', str(j))
                S3 = S3.replace('C', str(k))
                if int(S1)+int(S2) == int(S3):
                    return i,j,k
    return -1,-1,-1
S1 = input()
S2 = input()
S3 = input()
a,b,c = solve(S1, S2, S3)

if __name__ == '__main__':
    solve()