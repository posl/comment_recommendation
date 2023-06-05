Synthesizing 10/10 solutions

=======
Suggestion 1

def div(n):
    if n < 10:
        return 0
    s = str(n)
    l = len(s)
    res = 0
    for i in range(1,l):
        a = int(s[:i])
        b = int(s[i:])
        if a * b > res:
            res = a * b
    return res

=======
Suggestion 2

def main():
    N = input()
    n = len(N)
    ans = 0
    for i in range(1, n):
        A = int(N[:i])
        B = int(N[i:])
        ans = max(ans, A*B)
    print(ans)
main()

=======
Suggestion 3

def solve(n):
    n = str(n)
    ans = 0
    for i in range(1, len(n)):
        a = int(n[:i])
        b = int(n[i:])
        ans = max(ans, a * b)
    return ans

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if N == 4:
        print(4)
        return
    if N == 5:
        print(6)
        return
    if N == 6:
        print(9)
        return
    if N == 7:
        print(12)
        return
    if N == 8:
        print(18)
        return
    if N == 9:
        print(27)
        return
    if N == 10:
        print(36)
        return
    if N == 11:
        print(54)
        return
    if N == 12:
        print(81)
        return
    if N == 13:
        print(108)
        return
    if N == 14:
        print(162)
        return
    if N == 15:
        print(243)
        return
    if N == 16:
        print(324)
        return
    if N == 17:
        print(486)
        return
    if N == 18:
        print(729)
        return
    if N == 19:
        print(972)
        return
    if N == 20:
        print(1458)
        return
    if N == 21:
        print(2187)
        return
    if N == 22:
        print(2916)
        return
    if N == 23:
        print(4374)
        return
    if N == 24:
        print(6561)
        return
    if N == 25:
        print(8748)
        return
    if N == 26:
        print(13122)
        return
    if N == 27:
        print(19683)
        return
    if N == 28:
        print(26244)
        return
    if N == 29:
        print(39366)
        return
    if N == 30:
        print(59049)
        return
    if N == 31:
        print(78732)
        return
    if N == 32:
        print(118098)
        return

=======
Suggestion 5

def split(n):
    s=str(n)
    l=len(s)
    if l==1:
        return n
    if l==2:
        return n
    if l==3:
        return max(n//10,n%10)*max(n//10,n%10)*max(n//10,n%10)
    if l==4:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==5:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==6:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==7:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==8:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==9:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)
    if l==10:
        return max(n//10,n%10)*max(n//100,n%100)*max(n//100,n%100)

n=int(input())
print(split(n))

=======
Suggestion 6

def get_max_product(n):
    l = len(n)
    if l == 2:
        return int(n[0])*int(n[1])
    else:
        max_product = 0
        for i in range(1, l):
            n1 = n[:i]
            n2 = n[i:]
            if n1[0] != '0' and n2[0] != '0':
                product = int(n1)*int(n2)
                if max_product < product:
                    max_product = product
        return max_product

=======
Suggestion 7

def split(n):
    nstr = str(n)
    nlen = len(nstr)
    if nlen == 2:
        return [nstr[0], nstr[1]]
    elif nlen == 3:
        return [nstr[0], nstr[1:]]

    result = []
    for i in range(1, nlen):
        result.append([nstr[:i], nstr[i:]])
    return result

=======
Suggestion 8

def split(n):
    l = []
    while n:
        l.append(n%10)
        n //= 10
    l.reverse()
    return l

=======
Suggestion 9

def max_product(n):
    n_str = str(n)
    n_len = len(n_str)
    max_product = 0
    for i in range(1,n_len):
        a = int(n_str[:i])
        b = int(n_str[i:])
        product = a*b
        if product > max_product:
            max_product = product
    return max_product

=======
Suggestion 10

def splitNum(n):
    nStr = str(n)
    nLen = len(nStr)
    maxProduct = 0
    for i in range(1,nLen):
        num1 = nStr[0:i]
        num2 = nStr[i:nLen]
        product = int(num1)*int(num2)
        if product > maxProduct:
            maxProduct = product
    return maxProduct
