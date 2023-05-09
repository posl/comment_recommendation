def solve(n, x):
    x = sorted(x)
    m = x[n//2]
    return sum([(i-m)**2 for i in x])
n = int(input())
x = list(map(int, input().split()))
print(solve(n, x))

if __name__ == '__main__':
    solve()