def solve(k, x):
    result = []
    for i in range(x-k+1,x+k):
        result.append(i)
    return result

if __name__ == '__main__':
    solve()