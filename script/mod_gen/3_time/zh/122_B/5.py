def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            ok = True
            for k in range(i,j+1):
                if s[k] != 'A' and s[k] != 'C' and s[k] != 'G' and s[k] != 'T':
                    ok = False
            if ok:
                ans = max(ans,j-i+1)
    print(ans)

if __name__ == '__main__':
    main()