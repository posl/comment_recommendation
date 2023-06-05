def is_repdigit(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True
k = int(input())
cnt = 0
n = 0
while True:
    n += 1
    if is_repdigit(n):
        cnt += 1
    if cnt == k:
        break
print(n)

if __name__ == '__main__':
    is_repdigit()