def main():
    n,k = map(int, input().split())
    s = input()
    s = s.replace('RL','LR')
    s = s.replace('LR','RL')
    s = s.replace('LL','L')
    s = s.replace('RR','R')
    cnt = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt += 1
    print(min(n-1, cnt+2*k))

if __name__ == '__main__':
    main()