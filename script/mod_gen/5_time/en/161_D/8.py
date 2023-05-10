def lunlun(n):
    if n < 10:
        return n
    else:
        n = str(n)
        a = int(n[-1])
        if a == 9:
            return lunlun(int(n[:-1]))*10 + a
        else:
            return lunlun(int(n[:-1]))*10 + a - 1
K = int(input())
ans = 0
for i in range(K):
    ans = lunlun(ans+1)
print(ans)

if __name__ == '__main__':
    lunlun()