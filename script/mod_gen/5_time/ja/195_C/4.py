def comma_count(n):
    ans = 0
    for i in range(1, len(n)):
        ans += 9 * 10 ** (i - 1) * i
    ans += (int(n) - 10 ** (len(n) - 1) + 1) * len(n)
    return ans
n = input()
print(comma_count(n))

if __name__ == '__main__':
    comma_count()