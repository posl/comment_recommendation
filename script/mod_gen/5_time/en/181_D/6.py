def solve(s):
    if len(s) == 1:
        if s[0] == '8':
            return "Yes"
        else:
            return "No"
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return "Yes"
        else:
            return "No"
    else:
        cnt = [0] * 10
        for i in range(len(s)):
            cnt[int(s[i])] += 1
        for i in range(104, 1000, 8):
            t = [0] * 10
            t[0] = cnt[0]
            for j in range(3):
                t[i % 10] += cnt[i % 10]
                i //= 10
            if t[0] < cnt[0]:
                continue
            for j in range(10):
                if t[j] > cnt[j]:
                    break
            else:
                return "Yes"
        return "No"

if __name__ == '__main__':
    solve()