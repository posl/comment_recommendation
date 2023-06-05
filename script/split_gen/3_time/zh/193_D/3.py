def main():
    k = int(input())
    s = input()[:-1]
    t = input()[:-1]
    s = s.replace('#','')
    t = t.replace('#','')
    #print(s,t)
    s1 = [0]*10
    t1 = [0]*10
    for i in s:
        s1[int(i)] += 1
    for i in t:
        t1[int(i)] += 1
    #print(s1,t1)
    s2 = [0]*10
    t2 = [0]*10
    for i in range(1,10):
        s2[i] = k - s1[i]
        t2[i] = k - t1[i]
    #print(s2,t2)
    s3 = [0]*10
    t3 = [0]*10
    for i in range(1,10):
        for j in range(1,10):
            if i != j:
                if i > j:
                    s3[i] += s2[i]*t2[j]
                else:
                    t3[i] += s2[i]*t2[j]
    #print(s3,t3)
    s4 = 0
    t4 = 0
    for i in range(1,10):
        s4 += s1[i]*(i*10**s2[i])
        t4 += t1[i]*(i*10**t2[i])
    #print(s4,t4)
    s5 = 0
    t5 = 0
    for i in range(1,10):
        s5 += s3[i]*(i*10**s2[i])
        t5 += t3[i]*(i*10**t2[i])
    #print(s5,t5)
    s6 = 0
    t6 = 0
    for i in range(1,10):
        s6 += s3[i]*(i*10**s2[i])
        t6 += t3[i]*(i*10**t2[i])
    #print(s6,t6)
    s7 = 0
    t7 = 0
    for i in range(1,10):
        s7 += s3[i]*(i*10**s2[i])
        t7 += t3[i]*(i*10**t2[i
