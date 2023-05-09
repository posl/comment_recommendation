def count_hug(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            cnt += 1
    return cnt
s = input()
print(count_hug(s) // 2)

if __name__ == '__main__':
    count_hug()