def solve(n):
    # write your code here
    max = int(n**0.5)+1
    s = set()
    for i in range(2,max):
        for j in range(2,max):
            if pow(i,j) <= n:
                s.add(pow(i,j))
    return n - len(s) - 1

if __name__ == '__main__':
    solve()