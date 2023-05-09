def main():
    s = input()
    q = int(input())
    n = len(s)
    cnt = [0] * 3
    for i in range(n):
        cnt[ord(s[i]) - ord('A')] += 1
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        if t == 0:
            if k <= cnt[0]:
                print('A')
            elif k <= cnt[0] + cnt[1]:
                print('B')
            else:
                print('C')
        elif t == 1:
            if k <= cnt[1]:
                print('B')
            elif k <= cnt[0] + cnt[1]:
                print('C')
            else:
                print('A')
        else:
            if k <= cnt[2]:
                print('C')
            elif k <= cnt[0] + cnt[2]:
                print('A')
            else:
                print('B')
