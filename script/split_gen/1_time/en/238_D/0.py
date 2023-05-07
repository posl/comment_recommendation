def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        elif a == 0:
            print("No")
        elif s % 2 == 1:
            print("No")
        elif a % 2 == 0:
            print("Yes")
        elif s // 2 >= a:
            print("Yes")
        else:
            print("No")
main()
I don't know why I can't get this accepted. I tried to run this on my computer and it worked. I also tried to run it on the website and it worked. I also tried to submit it and it worked. I don't know why it's not working.
@kazutaka_kitamura
I'm not sure what you mean by "it worked". Did you get the correct answer?
If you did get the correct answer, then the problem is that the test cases are not public. This means that you can't see the test cases, and you can't be sure that your code works for all possible inputs.
So, you should submit your code anyway, and hope that it gets accepted. If it doesn't, you'll need to debug your code to find the bug.
I got the correct answer. I just don't know why it's not accepted.
I think I found the problem. I think it's because I'm using python 3.8.2 instead of python 3.6.5. I tried to submit it using python 3.6.5 and it worked. I don't know why it's not working with python 3.8.2.
@kazutaka_kitamura
It's not that it's not working with Python 3.8.2. It's that the test cases are not public, so we don't know what they are. So, we don't know whether your code will work for all possible inputs.
If you want to be sure that your code works for all possible inputs, you'll need to submit it anyway, and hope that it gets accepted. If it doesn't, you'll need to debug your code to find the bug.
I think I found the problem. I think it's because I'm using python 3.8.2 instead of python 3.6
