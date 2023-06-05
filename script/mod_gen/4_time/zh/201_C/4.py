def solve():
    s = input()
    count = 0
    for i in range(10000):
        s1 = str(i).zfill(4)
        flag = True
        for j in range(10):
            if s[j] == 'o' and str(j) not in s1:
                flag = False
            if s[j] == 'x' and str(j) in s1:
                flag = False
        if flag:
            count += 1
    print(count)
solve()
