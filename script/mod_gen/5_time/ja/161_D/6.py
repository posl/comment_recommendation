def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) > 1:
            return False
    return True
K = int(input())
cnt = 0
for i in range(10**20):
    if is_lunlun(i):
        cnt += 1
        if cnt == K:
            print(i)
            break

if __name__ == '__main__':
    is_lunlun()