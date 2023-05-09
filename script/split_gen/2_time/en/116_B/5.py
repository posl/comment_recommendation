def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
s=int(input())
a=[s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1])>1:
        break
print(len(a))
I think it's better to use a dictionary instead of a list in this case.
I think it's better to use a dictionary instead of a list in this case.
I agree with you. I will try it.
I agree with you. I will try it.
I have changed the code. I think it's better than before.
I hav
