def solve(a,s):
    if a == 0:
        if s == 0:
            return "Yes"
        else:
            return "No"
    if s < a:
        return "No"
    if s % 2 == 0 and a % 2 == 0:
        return "Yes"
    if s % 2 == 1 and a % 2 == 1:
        return "Yes"
    return "No"
T = int(input())
for _ in range(T):
    a,s = map(int,input().split())
    print(solve(a,s))

if __name__ == '__main__':
    solve()