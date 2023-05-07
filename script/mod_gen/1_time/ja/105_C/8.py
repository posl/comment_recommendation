def n2(num, base):
    if num == 0:
        return "0"
    ans = ""
    while num != 0:
        num, mod = divmod(num, base)
        if mod < 0:
            num, mod = num + 1, mod + abs(base)
        ans = str(mod) + ans
    return ans
num = int(input())
print(n2(num, -2))

if __name__ == '__main__':
    n2()