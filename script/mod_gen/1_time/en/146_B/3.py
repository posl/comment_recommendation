def shift(s, n):
    return ''.join([chr((ord(x) - ord('A') + n) % 26 + ord('A')) for x in s])
N = int(input())
S = input()
print(shift(S, N))
I have a problem with the following code. It works fine for the first test case but gives a wrong answer for the second test case. I don't know what's wrong with it. Can someone help me?
Here's the code:
n = int(input())
s = input()
s = s.upper()
l = []
for i in range(0,len(s)):
    if s[i] == " ":
        l.append(s[i])
    else:
        l.append(chr((ord(s[i])+n-65)%26+65))
print(*l, sep="")
Here's the first test case:
2
ABC XYZ
Here's the second test case:
3
ABC XYZ
Here's the output for the first test case:
CDE ZAB
Here's the output for the second test case:
DEF ZAB
I have a problem with the following code. It works fine for the first test case but gives a wrong answer for the second test case. I don't know what's wrong with it. Can someone help me?
Here's the code:
n = int(input())
s = input()
s = s.upper()
l = []
for i in range(0,len(s)):
    if s[i] == " ":
        l.append(s[i])
    else:
        l.append(chr((ord(s[i])+n-65)%26+65))
print(*l, sep="")
Here's the first test case:
2
ABC XYZ
Here's the second test case:
3
ABC XYZ
Here's the output for the first test case:
CDE ZAB
Here's the output for the second test case:
DEF ZAB
Here is the problem: https://atcoder.jp/contests/abc208/tasks/abc208_a
I am trying to solve this problem using Python. I have the following code:
a,b = map(int,input().split())

if __name__ == '__main__':
    shift()