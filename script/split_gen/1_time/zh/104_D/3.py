def main():
    s = input()
    len_s = len(s)
    q = s.count('?')
    mod = 10**9+7
    a = 0
    b = 0
    c = 0
    for i in range(len_s):
        if s[i] == 'A':
            a += 1
        elif s[i] == 'B':
            b += 1
        elif s[i] == 'C':
            c += 1
    ans = 0
    for i in range(q+1):
        for j in range(q-i+1):
            k = q-i-j
            ans += pow(3,i,mod)*pow(3,j,mod)*pow(3,k,mod)*\
                   (a+i)*(b+j)*(c+k)%mod
            ans %= mod
    print(ans)
