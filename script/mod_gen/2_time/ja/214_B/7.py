def main():
    s,t = map(int,input().split())
    n = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    n += 1
    print(n)

if __name__ == '__main__':
    main()