def modify_name(s, d):
    if s in d:
        d[s] += 1
        return s + "(" + str(d[s]) + ")"
    else:
        d[s] = 0
        return s
n = int(input())
d = {}
for i in range(n):
    s = input()
    print(modify_name(s, d))
