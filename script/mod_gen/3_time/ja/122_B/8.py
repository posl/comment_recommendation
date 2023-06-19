def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if set(s[i:j+1]) <= set('ACGT'):
                ans = max(ans,j-i+1)
    print(ans)
main()
