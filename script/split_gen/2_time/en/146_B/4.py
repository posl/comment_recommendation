def shift(s, n):
  return ''.join(chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s)
n = int(input())
s = input()
print(shift(s, n))
Python 3.6.1 (default, Apr  4 2017, 09:40:21) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import string
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> ord('A')
65
>>> ord('Z')
90
>>> ord('A') - ord('A')
0
>>> ord('A') - ord('A') + 1
1
>>> ord('Z') - ord('A') + 1
26
>>> ord('Z') - ord('A') + 2
27
>>> ord('Z') - ord('A') + 3
28
>>> ord('Z') - ord('A') + 4
29
>>> ord('Z') - ord('A') + 5
30
>>> ord('Z') - ord('A') + 6
31
>>> ord('Z') - ord('A') + 7
32
>>> ord('Z') - ord('A') + 8
33
>>> ord('Z') - ord('A') + 9
34
>>> ord('Z') - ord('A') + 10
35
>>> ord('Z') - ord('A') + 11
36
>>> ord('Z') - ord('A') + 12
37
>>> ord('Z') - ord('A') + 13
38
>>> ord('Z') - ord('A') + 14
39
>>> ord('Z') - ord('A') + 15
40
>>> ord('Z') - ord('A') + 16
41
>>> ord('Z') - ord('A') + 17
42
>>> ord('Z') - ord('A') + 18
43
>>> ord('Z') - ord('A') + 19
44
>>> ord('Z') - ord('A') + 20
45
>>>
