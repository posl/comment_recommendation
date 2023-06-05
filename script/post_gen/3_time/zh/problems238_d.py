Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if s < a:
            print('No')
        elif a == s:
            print('Yes')
        else:
            if s % 2 != a % 2:
                print('No')
            else:
                if s % 2 == 0:
                    print('Yes')
                else:
                    print('No')

=======
Suggestion 2

def solve(a, s):
    if s < a:
        return False
    if (s - a) % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 3

def isSum(a, s):
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return True
    if a == 1:
        return False
    if a == 2:
        return s % 2 == 0
    if a == 3:
        return s % 2 == 1
    if a == 4:
        return s % 2 == 0
    if a == 5:
        return s % 2 == 1
    if a == 6:
        return s % 2 == 0
    if a == 7:
        return s % 2 == 1
    if a == 8:
        return s % 2 == 0
    if a == 9:
        return s % 2 == 1
    if a == 10:
        return s % 2 == 0
    if a == 11:
        return s % 2 == 1
    if a == 12:
        return s % 2 == 0
    if a == 13:
        return s % 2 == 1
    if a == 14:
        return s % 2 == 0
    if a == 15:
        return s % 2 == 1
    if a == 16:
        return s % 2 == 0
    if a == 17:
        return s % 2 == 1
    if a == 18:
        return s % 2 == 0
    if a == 19:
        return s % 2 == 1
    if a == 20:
        return s % 2 == 0
    if a == 21:
        return s % 2 == 1
    if a == 22:
        return s % 2 == 0
    if a == 23:
        return s % 2 == 1
    if a == 24:
        return s % 2 == 0
    if a == 25:
        return s % 2 == 1
    if a == 26:
        return s % 2 == 0
    if a == 27:
        return s % 2 == 1
    if a == 28:
        return s

=======
Suggestion 4

def get_bit(num, pos):
    return (num >> pos) & 1

=======
Suggestion 5

def isBitwiseAnd(a, s):
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return False
    if s - a == a:
        return False
    if a & (s - a) == 0:
        return False
    return True

=======
Suggestion 6

def main():
    t = int(input())
    for i in range(t):
        a,s = input().split()
        a = int(a)
        s = int(s)
        if a > s:
            print('No')
        else:
            if (s-a)%2 == 0:
                print('Yes')
            else:
                print('No')

=======
Suggestion 7

def solve(a, s):
    if a > s:
        return 'No'
    if a == s:
        return 'Yes'
    if a == 0:
        return 'No'
    if a == 1:
        return 'Yes'
    if a == 2:
        return 'No'
    if a == 3:
        if s == 5:
            return 'Yes'
        else:
            return 'No'
    if a == 4:
        return 'No'
    if a == 5:
        if s == 8:
            return 'Yes'
        else:
            return 'No'
    if a == 6:
        return 'No'
    if a == 7:
        if s == 13:
            return 'Yes'
        else:
            return 'No'
    if a == 8:
        return 'No'
    if a == 9:
        if s == 17:
            return 'Yes'
        else:
            return 'No'
    if a == 10:
        return 'No'
    if a == 11:
        if s == 22:
            return 'Yes'
        else:
            return 'No'
    if a == 12:
        return 'No'
    if a == 13:
        if s == 26:
            return 'Yes'
        else:
            return 'No'
    if a == 14:
        return 'No'
    if a == 15:
        if s == 31:
            return 'Yes'
        else:
            return 'No'
    if a == 16:
        return 'No'
    if a == 17:
        if s == 35:
            return 'Yes'
        else:
            return 'No'
    if a == 18:
        return 'No'
    if a == 19:
        if s == 40:
            return 'Yes'
        else:
            return 'No'
    if a == 20:
        return 'No'
    if a == 21:
        if s == 44:
            return 'Yes'
        else:
            return 'No'
    if a == 22:
        return 'No'
    if a == 23:
        if s == 49:
            return 'Yes'
        else:
            return 'No'
    if a == 24:
        return 'No'
    if a == 25:

=======
Suggestion 8

def bit_sum(x):
    sum = 0
    while x != 0:
        sum += x % 2
        x /= 2
    return sum

=======
Suggestion 9

def solve(a, s):
    #print("a=%d, s=%d" % (a, s))
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return False
    
    x = a
    y = s - a
    if x & y == a:
        return True
    else:
        return False

=======
Suggestion 10

def main():
    T=int(input())
    for i in range(T):
        a,s=map(int,input().split())
        if a>s:
            print('No')
        elif a==s:
            print('Yes')
        else:
            k=s-a
            if k%2==0:
                print('Yes')
            else:
                print('No')
