def solve(n,vs):
    if n == 2:
        if vs[0] != vs[1]:
            return 0
        else:
            return 1
    else:
        count = 0
        for i in range(0,n,2):
            if vs[i] == vs[i+1]:
                count += 1
        return count

if __name__ == '__main__':
    solve()