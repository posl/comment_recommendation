def main():
    s = input()
    n = len(s)
    cnt0 = 0
    cnt1 = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            if s[i] == '1':
                cnt1 += 1
            else:
                cnt0 += 1
    print(min(cnt0, cnt1))
