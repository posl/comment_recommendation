def solve():
    s = input()
    if len(s) == 1:
        if s == '8':
            return 'Yes'
        else:
            return 'No'
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return 'Yes'
        else:
            return 'No'
    cnt = [0] * 10
    for c in s:
        cnt[int(c)] += 1
    for i in range(112, 1000, 8):
        tmp = [0] * 10
        tmp[i % 10] += 1
        tmp[i // 10 % 10] += 1
        tmp[i // 100] += 1
        flag = True
        for j in range(10):
            if tmp[j] > cnt[j]:
                flag = False
        if flag:
            return 'Yes'
    return 'No'
print(solve())

if __name__ == '__main__':
    solve()