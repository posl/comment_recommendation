def solve(a, s):
    # Write your code here
    if s < a:
        return "No"
    if s == a:
        return "Yes"
    if s & 1 == a & 1:
        return "Yes"
    return "No"

if __name__ == '__main__':
    solve()