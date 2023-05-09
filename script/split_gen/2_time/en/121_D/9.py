def f(A,B):
    if A==B:
        return A
    if A==0:
        return f(0,B)
    k=1
    while k<=B:
        k*=2
    k/=2
    if A>=k:
        return f(A-k,B-k)
    else:
        return k+f(0,B-k)
A,B=map(int,raw_input().split())
print f(A,B)
This is my first code in python. I tried to solve this problem with python, but I couldn't. I tried to use the same logic as my C++ code, but I couldn't. I think the problem is that I don't know how to use functions in python. I am really sorry, but I would appreciate it if you could help me with this problem.
I am sorry for my poor English.
