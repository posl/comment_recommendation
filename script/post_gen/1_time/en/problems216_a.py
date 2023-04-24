Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = input().split('.')
    y = int(y)
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + '+')

=======
Suggestion 2

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(x, '-', sep='')
    elif y <= 6:
        print(x)
    else:
        print(x, '+', sep='')

=======
Suggestion 3

def main():
    x, y = input().split(".")
    y = int(y)
    if y <= 2:
        print(x + "-")
    elif y <= 6:
        print(x)
    else:
        print(x + "+")

=======
Suggestion 4

def main():
    x, y = input().split('.')
    if int(y) <= 2:
        print(x + '-')
    elif int(y) <= 6:
        print(x)
    else:
        print(x + '+')

=======
Suggestion 5

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(x, '-', sep='')
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(x, '+', sep='')

main()

Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=3, releaselevel='final', serial=0)
>>> sys.version
'3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0]'

=======
Suggestion 6

def main():
    x = input()
    if x[-1] == '0' or x[-1] == '1' or x[-1] == '2':
        print(x[:-2] + '-')
    elif x[-1] == '3' or x[-1] == '4' or x[-1] == '5' or x[-1] == '6':
        print(x[:-2])
    elif x[-1] == '7' or x[-1] == '8' or x[-1] == '9':
        print(x[:-2] + '+')

main()

=======
Suggestion 7

def main():
    x = input()
    x = x.split('.')
    if int(x[1]) <= 2:
        print(x[0]+'-')
    elif int(x[1]) <= 6:
        print(x[0])
    else:
        print(x[0]+'+')

main()

=======
Suggestion 8

def main():
    x = raw_input().split('.')
    y = int(x[1])
    if y <= 2:
        print x[0]+'-'
    elif y <= 6:
        print x[0]
    else:
        print x[0]+'+'

=======
Suggestion 9

def main():
    # Write your code here
    x = input()
    if x[-1] in "012":
        print(x[:-2]+"-")
    elif x[-1] in "3456":
        print(x[:-2])
    else:
        print(x[:-2]+"+")
main()

I am a Python Developer and a Competitive Programmer. I have been programming since I was 13 years old. I have participated in many coding competitions and have solved many problems in different programming languages. I am a self taught programmer. I believe in sharing knowledge and helping others.

=======
Suggestion 10

def main():
    #x, y = list(map(int, input().split('.')))
    #print(x, y)
    x, y = input().split('.')
    y = int(y)
    if y >= 0 and y <= 2:
        print(x + '-')
    elif y >= 3 and y <= 6:
        print(x)
    else:
        print(x + '+')
