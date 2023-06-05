def main():
    s = input()
    k = int(input())
    n = len(s)
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    print(min(n-1, cnt+2*k))

if __name__ == '__main__':
    main()