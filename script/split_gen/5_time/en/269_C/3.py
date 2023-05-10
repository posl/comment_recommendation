def main():
    n = int(input())
    l = []
    for i in range(60):
        if n & (1 << i):
            l.append(i)
    #print(l)
    ans = []
    for i in range(1 << len(l)):
        tmp = 0
        for j in range(len(l)):
            if i & (1 << j):
                tmp += 1 << l[j]
        if tmp <= n:
            ans.append(tmp)
    ans.sort()
    for i in ans:
        print(i)
