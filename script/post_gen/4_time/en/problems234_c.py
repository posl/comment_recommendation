Synthesizing 10/10 solutions

=======
Suggestion 1

def base2(n):
    if n == 0:
        return '0'
    else:
        s = ''
        while n > 0:
            s = str(n % 2) + s
            n = n // 2
        return s

=======
Suggestion 2

def problem():
    K = int(input())

    # 0, 2, 20, 22, 200, 202, 220, 222, 2000, 2002, 2020, 2022, 2200, 2202, 2220, 2222, 20000, 20002, 20020, 20022, 20200, 20202, 20220, 20222, 22000, 22002, 22020, 22022, 22200, 22202, 22220, 22222
    # 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19

    # 0, 2, 20, 22, 200, 202, 220, 222, 2000, 2002, 2020, 2022, 2200, 2202, 2220, 2222, 20000, 20002, 20020, 20022, 20200, 20202, 20220, 20222, 22000, 22002, 22020, 22022, 22200, 22202, 22220, 22222
    # 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19

    # 0, 2, 20, 22, 200, 202, 220, 222, 2000, 2002, 2020, 2022, 2200, 2202, 2220, 2222, 20000, 20002, 20020, 20022, 20200, 20202, 20220, 20222, 22000, 22002, 22020, 22022, 22200, 22202, 22220, 22222
    # 0, 1, 2, 3, 4, 7, 8, 9,

=======
Suggestion 3

def main():
    K = int(input())
    if K == 1:
        print(2)
        return
    else:
        K -= 1
        ans = ''
        while K > 0:
            ans = str(K % 2) + ans
            K //= 2
        ans = ans.replace('0', '2')
        print(ans)

=======
Suggestion 4

def solve(k):
    if k == 1:
        return 2
    else:
        return 10 * solve(k - 1) + 2

=======
Suggestion 5

def main():
    k = int(input())
    #print(k)
    #print(type(k))
    #print(bin(k))
    #print(type(bin(k)))
    #print(bin(k)[2:])
    #print(type(bin(k)[2:]))
    #print(len(bin(k)[2:]))
    #print(type(len(bin(k)[2:])))
    #print(bin(k)[2:].count('0'))
    #print(type(bin(k)[2:].count('0')))
    #print(bin(k)[2:].count('2'))
    #print(type(bin(k)[2:].count('2')))
    #print(bin(k)[2:].count('0') + bin(k)[2:].count('2'))
    #print(type(bin(k)[2:].count('0') + bin(k)[2:].count('2')))
    #print(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:]))
    #print(type(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:])))
    #print(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:]) and bin(k)[2:].count('2') == 1)
    #print(type(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:]) and bin(k)[2:].count('2') == 1))
    #print(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:]) and bin(k)[2:].count('2') == 1 and bin(k)[2:].count('0') == 0)
    #print(type(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:]) and bin(k)[2:].count('2') == 1 and bin(k)[2:].count('0') == 0))
    #print(bin(k)[2:].count('0') + bin(k)[2:].count('2') == len(bin(k)[2:]) and bin(k)[2:].count('2') == 1 and bin(k)[2:].count('0') == 0 and k % 2 == 0)
    #print(type(bin(k)[2:].

=======
Suggestion 6

def main():
    K = int(input())
    ans = 0
    for i in range(1, 1000000):
        if '2' in str(i):
            ans += 1
            if ans == K:
                print(i)
                exit()

=======
Suggestion 7

def findKthInteger(k):
    k -= 1
    ans = ""
    while k:
        ans += str(k % 2 * 2)
        k //= 2
    return ans[::-1].replace("0", "2")

k = int(input())
print(findKthInteger(k))

=======
Suggestion 8

def main():
    K = int(input())
    print(int("".join(["2" if i % 2 == 0 else "0" for i in range(K)])))

=======
Suggestion 9

def main():
    K = int(input())
    print(base10to2(K))

=======
Suggestion 10

def get_number_of_2s(number):
    return str(number).count('2')
