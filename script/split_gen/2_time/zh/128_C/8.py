def main():
    n, m = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        tmp = list(map(int, input().split()))
        k.append(tmp[0])
        s.append(tmp[1:])
    p = list(map(int, input().split()))
    #print(n, m, k, s, p)
    #num = 0
    #for i in range(2**n):
    #    tmp = []
    #    for j in range(n):
    #        tmp.append(i%2)
    #        i //= 2
    #    #print(tmp)
    #    flag = True
    #    for j in range(m):
    #        count = 0
    #        for l in s[j]:
    #            count += tmp[l-1]
    #        if count % 2 != p[j]:
    #            flag = False
    #            break
    #    if flag:
    #        num += 1
    #print(num)
    num = 0
    for i in range(2**n):
        tmp = []
        for j in range(n):
            tmp.append(i%2)
            i //= 2
        #print(tmp)
        flag = True
        for j in range(m):
            count = 0
            for l in s[j]:
                count += tmp[l-1]
            if count % 2 != p[j]:
                flag = False
                break
        if flag:
            num += 1
    print(num)
