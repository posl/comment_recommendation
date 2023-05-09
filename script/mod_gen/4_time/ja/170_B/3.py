def solve():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i*4 + (x-i)*2 == y:
            return "Yes"
    return "No"
print(solve())

if __name__ == '__main__':
    solve()