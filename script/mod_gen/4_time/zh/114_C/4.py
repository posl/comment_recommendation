def count753(n, num):
    if num > n:
        return 0
    ret = 1 if num >= 357 else 0
    ret += count753(n, num * 10 + 3)
    ret += count753(n, num * 10 + 5)
    ret += count753(n, num * 10 + 7)
    return ret
n = int(input())
print(count753(n, 0))
