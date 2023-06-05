def solve(n, xs, ys):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if xs[i] == xs[j] or ys[i] == ys[j]:
                count += 1
    return count

if __name__ == '__main__':
    solve()