def main():
    S = input()
    N = len(S)
    cnt0 = 0
    cnt1 = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            if S[i] == '0':
                cnt1 += 1
            else:
                cnt0 += 1
    print(min(cnt0, cnt1))
