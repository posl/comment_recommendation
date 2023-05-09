def main():
    K = int(input())
    S = input()
    T = input()
    S = S[:-1]
    T = T[:-1]
    #print(S)
    #print(T)
    s = 0
    t = 0
    c = [0]*10
    for i in range(4):
        c[int(S[i])] += 1
        c[int(T[i])] += 1
    for i in range(1,10):
        s += i*10**(c[i])
        t += i*10**(c[i])
    #print(c)
    #print(s)
    #print(t)
    p = 0
    for i in range(1,10):
        for j in range(1,10):
            if s + i*10**(c[i]+1) > t + j*10**(c[j]+1):
                if i==j:
                    p += (K-c[i])*(K-c[i]-1)/(K*(K-1))
                else:
                    p += (K-c[i])*(K-c[j])/(K*(K-1))
    print(p)
