def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    cnt = [0, 0, 0]
    for i in range(3):
        cnt[i] = S.count(chr(ord('A') + i))
    for t, k in query:
        t %= 3
        if t == 0:
            print(S[k - 1])
        else:
            k -= 1
            k = (k + cnt[t - 1]) % (cnt[0] + cnt[1] + cnt[2])
            if k < cnt[0]:
                print('A')
            elif k < cnt[0] + cnt[1]:
                print('B')
            else:
                print('C')
