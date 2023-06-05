def solve(S1, S2, S3):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                N1 = S1.replace('a', str(i)).replace('b', str(j)).replace('c', str(k))
                N2 = S2.replace('a', str(i)).replace('b', str(j)).replace('c', str(k))
                N3 = S3.replace('a', str(i)).replace('b', str(j)).replace('c', str(k))
                if N1[0] == '0' or N2[0] == '0' or N3[0] == '0':
                    continue
                if int(N1) + int(N2) == int(N3):
                    return N1, N2, N3
    return None, None, None

if __name__ == '__main__':
    solve()