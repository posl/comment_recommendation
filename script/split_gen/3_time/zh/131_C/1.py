def problem131_c():
    a,b,c,d = map(int,input().split())
    cnt = 0
    for i in range(a,b+1):
        if i % c == 0 and i % d == 0:
            cnt += 1
    print(cnt)
