def solve(a,s):
    if a>s:
        return 'No'
    if a==s:
        return 'Yes'
    if a==0:
        return 'No'
    if a==1:
        return 'Yes'
    if s%2==0:
        return 'Yes'
    if a%2==0:
        return 'Yes'
    return 'No'
T = int(input())
for i in range(T):
    a,s = [int(x) for x in input().split()]
    print(solve(a,s))

if __name__ == '__main__':
    solve()