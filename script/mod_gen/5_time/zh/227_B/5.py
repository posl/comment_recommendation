def check(a, b, s):
    if 4 * a * b + 3 * a + 3 * b == s:
        return True
    else:
        return False
n = int(input())
s = list(map(int, input().split()))
count = 0
for i in range(n):
    for a in range(1, s[i] + 1):
        for b in range(1, s[i] + 1):
            if check(a, b, s[i]):
                count += 1
print(n - count)

if __name__ == '__main__':
    check()