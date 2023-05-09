def main():
    n,k = map(int,input().split())
    s = input()
    #print(n,k,s)
    s = s.replace('0','1').replace('1','0')
    #print(s)
    s = s.split('1')
    #print(s)
    s.sort()
    #print(s)
    s.reverse()
    #print(s)
    ans = 0
    for i in range(min(k,len(s))):
        ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()