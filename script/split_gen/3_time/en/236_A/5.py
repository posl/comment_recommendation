def swap(s, a, b):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return "".join(s)
S = input()
a, b = map(int, input().split())
print(swap(S, a-1, b-1))
I’m not sure why I got this error when I tried to submit my code.
“Traceback (most recent call last): File “”, line 1, in ImportError: No module named ‘_codecs_cn’”
I got the same error, but I have no idea what it means.
I got the sam
