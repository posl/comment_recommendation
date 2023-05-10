def is753(n):
    s = str(n)
    return s.count('7') and s.count('5') and s.count('3') and not s.count('0') and not s.count('1') and not s.count('2') and not s.count('4') and not s.count('6') and not s.count('8') and not s.count('9')
n = int(input())
ans = 0
for i in range(1, n+1):
    if is753(i):
        ans += 1
print(ans)
