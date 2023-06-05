def main():
    n,m = map(int,raw_input().split())
    work = []
    for i in range(n):
        work.append(map(int,raw_input().split()))
    work.sort(key=lambda x:x[0])
    #print work
    ans = 0
    for i in range(n):
        if m >= work[i][0]:
            m -= work[i][0]
            ans += work[i][1]
    print ans

if __name__ == '__main__':
    main()