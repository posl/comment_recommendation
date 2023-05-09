def problem285_c():
    S = input()
    l = len(S)
    ans = 0
    for i in range(l):
        ans += (ord(S[i])-ord('A')+1)*26**(l-i-1)
    print(ans)

if __name__ == '__main__':
    problem285_c()