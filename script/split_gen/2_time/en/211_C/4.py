def main():
    S = input()
    mod = 10**9 + 7
    num = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(S)):
        if S[i] == 'c':
            num[0] += 1
        elif S[i] == 'h':
            num[1] += num[0]
        elif S[i] == 'o':
            num[2] += num[1]
        elif S[i] == 'k':
            num[3] += num[2]
        elif S[i] == 'u':
            num[4] += num[3]
        elif S[i] == 'd':
            num[5] += num[4]
        elif S[i] == 'a':
            num[6] += num[5]
        elif S[i] == 'i':
            num[7] += num[6]
    print(num[7] % mod)
