def solve():
    v,a,b,c = map(int,input().split())
    if v <= a:
        return "F"
    if v <= a+b:
        return "M"
    return "T"
print(solve())

if __name__ == '__main__':
    solve()