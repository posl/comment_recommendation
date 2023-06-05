def solve(N, M, k, s, p):
    result = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for l in range(k[j]):
                if (i >> (s[j][l]-1) & 1):
                    count += 1
            if (count % 2 != p[j]):
                flag = False
                break
        if (flag):
            result += 1
    return result

if __name__ == '__main__':
    solve()