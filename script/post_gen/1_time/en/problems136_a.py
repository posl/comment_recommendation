Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A - B >= C:
        print(0)
    else:
        print(C - (A - B))

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if C > A - B:
        print(C - (A - B))
    else:
        print(C)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if (A - B) > C:
        print(0)
    else:
        print(C - (A - B))

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    if (A-B) >= C:
        print(0)
    else:
        print(C-(A-B))

=======
Suggestion 6

def main():
    # Write your code here
    A, B, C = map(int, input().split())
    if A - B >= C:
        print(0)
    else:
        print(C - (A - B))

=======
Suggestion 7

def main():
    # put your code here
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    print(a-b if a-b<c else c)

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if a - b < c else 0)

main()

Hi, I am a student from India. I am interested in competitive programming and I am trying to learn Python. I am a beginner and I am trying to solve problems from AtCoder. I am trying to solve this problem https://atcoder.jp/contests/abc136/tasks/abc136_a. I am able to solve it using C++ but I am not able to solve it using Python. I am not able to understand the error I am getting. I am getting this error when I am trying to submit my code. I am getting this error:

Traceback (most recent call last):
  File "/home/runner/work/abc136/abc136/a.py", line 13, in <module>
    main()
  File "/home/runner/work/abc136/abc136/a.py", line 11, in main
    print(c - (a - b) if a - b < c else 0)
NameError: name 'a' is not defined

I am not able to understand what is the problem. Can anyone please help me?

Thank you.

Your code is not indented properly. This is the reason why it is giving error. You can see that the code is not properly indented here. You can indent the code by using tab key.

Thank you @SanketSahu for your reply. I am sorry I didn't notice that. I have fixed it. But I am still getting the same error. Can you please help me?

I am not able to understand what is the problem. Can anyone please help me?

Thank you.

You need to indent the code properly. You can do that by using tab key. The code is not indented properly here.

Thank you @SanketSahu for your reply. I am sorry I didn't notice that. I have fixed it. But I am still getting the same error. Can you please help me?

You need to indent the code properly. You can do that by using tab key. The code is not indented properly here.

Thank you @SanketSahu for your reply. I am sorry I didn't notice that. I have fixed it. But I am still getting the same error. Can you please help me?

You need to indent the
