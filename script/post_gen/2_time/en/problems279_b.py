Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()

    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S.find(T) == -1:
        print("No")
    else:
        print("Yes")

main()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_contiguous_substring(s, t):
    if s == t:
        return True
    elif len(s) == 1:
        return False
    else:
        if s[0] == t[0]:
            return is_contiguous_substring(s[1:], t[1:])
        elif s[-1] == t[0]:
            return is_contiguous_substring(s[:-1], t[1:])
        else:
            return False

=======
Suggestion 8

def   is_contiguous_substring ( s ,   t ): 
     if   s   ==   t : 
         return   'Yes' 
     if   len ( s )   <   len ( t ): 
         return   'No' 
     if   s [ 0 ]   ==   t [ 0 ]: 
         return   is_contiguous_substring ( s [ 1 :],   t [ 1 :]) 
     if   s [ - 1 ]   ==   t [ 0 ]: 
         return   is_contiguous_substring ( s [ 0 : - 1 ],   t [ 1 :]) 
     return   'No'

=======
Suggestion 9

def isSubString(s, t):
    if s == t:
        return True
    elif len(s) == 1:
        return False
    else:
        if s[0] == t[0]:
            return isSubString(s[1:], t[1:])
        elif s[-1] == t[0]:
            return isSubString(s[:-1], t[1:])
        else:
            return False

s = input()
t = input()

=======
Suggestion 10

def check_substring(S, T):
    if len(S) < len(T):
        return "No"
    if S == T:
        return "Yes"
    for i in range(len(S) - len(T) + 1):
        if S[i:i + len(T)] == T:
            return "Yes"
    return "No"
