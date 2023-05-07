def solve(a,s):
    if a>s:
        return "No"
    if a==s:
        return "Yes"
    if a==0:
        if s==0:
            return "Yes"
        else:
            return "No"
    if s%2==0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    solve()