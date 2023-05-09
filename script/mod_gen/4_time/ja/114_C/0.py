def is753(n):
    s = str(n)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0 and s.count('4') == 0 and s.count('6') == 0 and s.count('8') == 0 and s.count('9') == 0
n = int(input())
cnt = 0
for i in range(1, n + 1):
    if is753(i):
        cnt += 1
print(cnt)

if __name__ == '__main__':
    is753()