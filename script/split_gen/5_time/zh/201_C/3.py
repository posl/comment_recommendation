def solve():
    s = input()
    cnt = 0
    for i in range(10000):
        flag = True
        for j in range(10):
            if s[j] == "o" and str(j) not in str(i):
                flag = False
            elif s[j] == "x" and str(j) in str(i):
                flag = False
        if flag:
            cnt += 1
    print(cnt)
solve()
