def solve(x):
    balance = 100
    years = 0
    while balance < x:
        balance += balance // 100
        years += 1
    return years

if __name__ == '__main__':
    solve()