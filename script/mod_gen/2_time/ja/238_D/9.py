def solve(a,s):
    if a>s:
        return "No"
    if a==s:
        if a==0:
            return "Yes"
        return "No"
    if (s-a)&1==1:
        return "No"
    return "Yes"

if __name__ == '__main__':
    solve()