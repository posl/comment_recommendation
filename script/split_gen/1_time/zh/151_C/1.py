def solution():
    n,m = map(int, input().split())
    problem = [0]*n
    ac = 0
    wa = 0
    for i in range(m):
        p,s = input().split()
        p = int(p)
        if problem[p-1] == 0 and s == "AC":
            problem[p-1] = 1
            ac += 1
        elif s == "WA" and problem[p-1] == 0:
            wa += 1
    print(ac,wa)
solution()
