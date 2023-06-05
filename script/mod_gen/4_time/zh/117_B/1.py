def judge_polygon(n, l):
    l.sort()
    l.reverse()
    #print(l)
    if l[0] >= sum(l[1:]):
        return "否"
    else:
        return "是"
n = int(input())
l = list(map(int, input().split()))
print(judge_polygon(n, l))
