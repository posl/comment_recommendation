def shift(s, n):
    if n == 0:
        return s
    if n > 26:
        n = n % 26
    s = list(s)
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    return ''.join(s)
N = int(input())
S = input()
print(shift(S, N))
This is my code for this problem.
I'm not sure if this is the best solution, but it works.
I'm interested in your opinion.
Thanks.
I think it is good. I think it is good.
I think it is good.
