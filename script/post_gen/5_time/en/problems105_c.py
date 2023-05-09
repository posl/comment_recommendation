Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
        else:
            ans.append(1)
            n -= 1
        n //= -2
    ans.reverse()
    print(''.join(map(str, ans)))

=======
Suggestion 2

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n = n // (-2)
        else:
            ans.append(1)
            n = (n - 1) // (-2)
    print(''.join(map(str, ans[::-1])))

=======
Suggestion 3

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    s = ''
    while n != 0:
        if n % 2 == 0:
            s = '0' + s
            n = n // -2
        else:
            s = '1' + s
            n = (n - 1) // -2
    print(s)

=======
Suggestion 4

def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n //= -2
        else:
            ans.append(1)
            n = (n - 1) // -2
    ans.reverse()
    print(''.join(map(str, ans)))

=======
Suggestion 5

def base_minus_2(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 == 0:
            s = '0' + s
            n //= -2
        else:
            s = '1' + s
            n = (n - 1) // -2
    return s

n = int(input())
print(base_minus_2(n))

=======
Suggestion 6

def base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(str(X)[-i]) * (n**(i-1))
    return out

=======
Suggestion 7

def base_minus2(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 != 0:
            s += '1'
            n -= 1
        else:
            s += '0'
        n //= -2
    return s[::-1]

n = int(input())
print(base_minus2(n))

=======
Suggestion 8

def base_neg2(n):
    if n == 0:
        return "0"
    ret = ""
    while n != 0:
        if n % 2 == 0:
            ret += "0"
        else:
            ret += "1"
            n -= 1
        n //= -2
    return ret[::-1]

=======
Suggestion 9

def solution(n):
    if n == 0:
        return 0

    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append("0")
            n //= -2
        else:
            ans.append("1")
            n = (n-1) // -2
    ans.reverse()
    return "".join(ans)

=======
Suggestion 10

def base_minus_2(n):
    if n==0:
        return 0
    else:
        s=''
        while n!=0:
            if n%2==0:
                s+='0'
                n=n//2
            else:
                s+='1'
                n=(n-1)//(-2)
        return s[::-1]
n=int(input())
print(base_minus_2(n))
