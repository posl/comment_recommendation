def solve():
    s = input()
    odd = ''
    even = ''
    for i in range(len(s)):
        if i % 2 == 0:
            odd += s[i]
        else:
            even += s[i]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')
solve()
