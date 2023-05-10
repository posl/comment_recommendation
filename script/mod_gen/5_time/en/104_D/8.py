def getABCNumber(s):
    abc = 0
    q = 0
    for i in range(len(s)):
        if s[i] == 'A':
            abc += q
        elif s[i] == 'B':
            q += abc
        elif s[i] == 'C':
            q = q
        else:
            abc = abc * 3 + q
            q = q * 3
        abc %= 1000000007
        q %= 1000000007
    return abc
s = input()
print(getABCNumber(s))

if __name__ == '__main__':
    getABCNumber()