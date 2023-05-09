def longestACGT(s):
    count = 0
    maxcount = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            count += 1
        else:
            count = 0
        if count > maxcount:
            maxcount = count
    return maxcount
s = input()
print(longestACGT(s))
I got the following error message:
Traceback (most recent call last):
  File "problems122_b.py", line 38, in <module>
    print(longestACGT(s))
  File "problems122_b.py", line 31, in longestACGT
    if i == "A" or i == "C" or i == "G" or i == "T":
TypeError: 'bool' object is not iterable
I am not sure why it is saying that bool is not iterable. I am new to python so I am not sure what that means. I am also not sure why the code is not working, I am sure it is a simple mistake. Any help would be greatly appreciated. Thanks!
If you want to see the error message, you can add a print statement just before the error line:
print(i)
This will print the value of i before the error occurs. You should get a result like:
ATCODER
A
T
C
O
D
E
R
In your case, i is a bool , which is not iterable. This means that it can't be used in a for loop. You probably want to use a while loop instead.
To see what the error is, you can add a print statement just before the error line:
print(i)
This will print the value of i before the error occurs. You should get a result like:
ATCODER
A
T
C
O
D
E
R
In your case, i is a bool , which is not iterable. This means that it can't be used in a for loop. You probably want to use a while loop instead.
I got the following error message:
Traceback (most recent call last):
  File "problems122_b.py", line 38, in <module>
    print(longestACGT(s))
  File "problems122_b.py", line 31, in longestACGT
    if i == "A" or
