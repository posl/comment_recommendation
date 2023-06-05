Synthesizing 10/10 solutions

=======
Suggestion 1

def to_base2(n):
    if n == 0:
        return '0'
    s = ''
    while n != 0:
        if n % 2 == 0:
            s = '0' + s
        else:
            s = '1' + s
            n -= 1
        n /= -2
    return s

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
            n //= -2
        else:
            ans.append(1)
            n = (n - 1) // -2
    print(''.join(map(str, ans[::-1])))

=======
Suggestion 3

def main():
    n = int(input())
    if n == 0:
        print(0)
        return

    s = ""
    while n != 0:
        if n % 2 == 0:
            s = "0" + s
        else:
            s = "1" + s
            n -= 1
        n //= -2
    print(s)

=======
Suggestion 4

def baseNeg2(N):
    if N == 0:
        return '0'
    res = ''
    while N != 0:
        res = str(N % 2) + res
        N = -(N // 2)
    return res

=======
Suggestion 5

def get_base_minus_2(n):
    if n == 0:
        return 0
    else:
        return n % (-2) + 10 * get_base_minus_2(-(n - n % (-2)) // 2)

=======
Suggestion 6

def convertToBaseNeg2(N):
    if (N == 0):
        return '0'
    ans = ''
    while (N != 0):
        rem = N % (-2)
        N = N // (-2)
        if (rem < 0):
            rem += 2
            N += 1
        ans = str(rem) + ans
    return ans

N = int(input())
print(convertToBaseNeg2(N))

=======
Suggestion 7

def baseNeg2(N):
    if N == 0:
        return '0'
    res = ''
    while N != 0:
        res = str(N % (-2)) + res
        N = -(N // (-2))
    return res

=======
Suggestion 8

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n = n // -2
        else:
            ans.append(1)
            n = (n - 1) // -2
    ans.reverse()
    print(''.join(map(str, ans)))

=======
Suggestion 9

def main():
    n = int(input())
    if n == 0:
        print(0)
    else:
        s = []
        while n != 0:
            if n % 2 == 0:
                s.append('0')
                n = n // -2
            else:
                s.append('1')
                n = (n - 1) // -2
        print(''.join(s[::-1]))

=======
Suggestion 10

def base_2(n):
    if n == 0:
        return 0
    else:
        return base_2(n//(-2)) + str(n%(-2))
