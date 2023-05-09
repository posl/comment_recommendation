def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    if x <= 1:
        return 0
    if x <= 1 + (2 ** (n-1)) - 1:
        return burger(n-1,x-1)
    if x == 1 + (2 ** (n-1)):
        return 2 ** (n-1)
    if x <= 1 + (2 ** (n-1)) * 2 - 1:
        return 2 ** (n-1) + burger(n-1,x-1-(2 ** (n-1)))
    if x == 1 + (2 ** (n-1)) * 2:
        return 2 ** (n)
N,X = map(int,input().split())
print(burger(N,X))
I think this is the first time I've ever used recursion in a contest. I've never actually used it in a real program before, either. This is a pretty cool problem, and I'm glad I got to solve it. I'm looking forward to the next contest.
