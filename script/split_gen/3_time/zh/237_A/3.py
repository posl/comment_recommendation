def is_between(n):
    if -2**31 <= n and n <= 2**31-1:
        print('是')
    else:
        print('否')
n = int(input())
is_between(n)
