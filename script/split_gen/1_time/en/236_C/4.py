def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    ans = ['No']*n
    for i in range(n):
        if s[i] in t:
            ans[i] = 'Yes'
    print('
'.join(ans))
